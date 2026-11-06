Add-Type -AssemblyName System.Drawing

$outDir = Join-Path $PSScriptRoot 'figures'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

function New-Canvas([int]$width, [int]$height) {
    $bmp = New-Object System.Drawing.Bitmap($width, $height)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g.Clear([System.Drawing.Color]::White)
    return @($bmp, $g)
}

function Save-Canvas($bmp, $g, [string]$name) {
    $g.Dispose()
    $path = Join-Path $outDir $name
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
}

$axisPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(65,65,65), 2)
$gridPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(220,220,220), 1)
$font = New-Object System.Drawing.Font('Arial', 21)
$smallFont = New-Object System.Drawing.Font('Arial', 18)
$tinyFont = New-Object System.Drawing.Font('Arial', 15, [System.Drawing.FontStyle]::Bold)
$titleFont = New-Object System.Drawing.Font('Arial', 25, [System.Drawing.FontStyle]::Bold)
$valueFont = New-Object System.Drawing.Font('Arial', 19, [System.Drawing.FontStyle]::Bold)
$textBrush = [System.Drawing.Brushes]::Black
$seriesColors = @(
    [System.Drawing.Color]::FromArgb(76,120,168),
    [System.Drawing.Color]::FromArgb(242,207,91),
    [System.Drawing.Color]::FromArgb(228,87,86)
)

# Label distribution ---------------------------------------------------------
$canvas = New-Canvas 1600 620
$bmp = $canvas[0]; $g = $canvas[1]
$panels = @(
    @{Title='North-targeted labels'; Values=@(3674,263,486)},
    @{Title='South-targeted labels'; Values=@(4235,89,99)}
)
$labels = @('NON_HATE','PREJUDICIAL','HOSTILE')
for ($p=0; $p -lt 2; $p++) {
    $left = 90 + 790*$p; $top=75; $w=680; $h=410; $bottom=$top+$h
    $g.DrawString($panels[$p].Title, $titleFont, $textBrush, $left+185, 20)
    for ($t=0; $t -le 4; $t++) {
        $y=$bottom-$t*($h/4); $g.DrawLine($gridPen,$left,$y,$left+$w,$y)
        $g.DrawString(([string]($t*1125)), $smallFont, $textBrush, $left-70, $y-12)
    }
    $g.DrawLine($axisPen,$left,$top,$left,$bottom); $g.DrawLine($axisPen,$left,$bottom,$left+$w,$bottom)
    for ($i=0; $i -lt 3; $i++) {
        $barW=150; $x=$left+55+$i*210; $val=$panels[$p].Values[$i]; $barH=$val/4500*$h; $y=$bottom-$barH
        $brush=New-Object System.Drawing.SolidBrush($seriesColors[$i]); $g.FillRectangle($brush,$x,$y,$barW,$barH); $brush.Dispose()
        $s=$val.ToString('N0'); $sz=$g.MeasureString($s,$valueFont); $g.DrawString($s,$valueFont,$textBrush,$x+($barW-$sz.Width)/2,$y-32)
        $sz=$g.MeasureString($labels[$i],$smallFont); $g.DrawString($labels[$i],$smallFont,$textBrush,$x+($barW-$sz.Width)/2,$bottom+15)
    }
}
Save-Canvas $bmp $g 'label_distribution_en.png'

# Comment-length distribution -----------------------------------------------
# Length is measured in Unicode string characters.  The panels mirror the
# target-specific label structure used in the manuscript.
$allRows = @()
foreach ($file in @('train.csv','val.csv','test.csv')) {
    $allRows += Import-Csv -LiteralPath (Join-Path $PSScriptRoot ('data\processed\' + $file))
}
$lengthPanels = @(
    @{Title='Entire corpus'; Rows=@($allRows); Color=[System.Drawing.Color]::FromArgb(220,45,45)},
    @{Title='North: NON_HATE'; Rows=@($allRows | Where-Object {$_.north_hate -eq 'NON_HATE'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='North: PREJUDICIAL'; Rows=@($allRows | Where-Object {$_.north_hate -eq 'PREJUDICIAL'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='North: HOSTILE'; Rows=@($allRows | Where-Object {$_.north_hate -eq 'HOSTILE'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='South: NON_HATE'; Rows=@($allRows | Where-Object {$_.south_hate -eq 'NON_HATE'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='South: PREJUDICIAL'; Rows=@($allRows | Where-Object {$_.south_hate -eq 'PREJUDICIAL'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='South: HOSTILE'; Rows=@($allRows | Where-Object {$_.south_hate -eq 'HOSTILE'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)},
    @{Title='Any harmful target'; Rows=@($allRows | Where-Object {$_.north_hate -ne 'NON_HATE' -or $_.south_hate -ne 'NON_HATE'}); Color=[System.Drawing.Color]::FromArgb(30,55,215)}
)
$canvas = New-Canvas 2000 980
$bmp = $canvas[0]; $g = $canvas[1]
$cols = 4; $panelW = 470; $panelH = 380; $plotW = 390; $plotH = 270
$edges = @(0,20,40,60,80,100,120,140,160,180,200,220,240,260)
$binCount = $edges.Count - 1
for ($i=0; $i -lt $lengthPanels.Count; $i++) {
    $panel = $lengthPanels[$i]
    $col = $i % $cols; $row = [math]::Floor($i / $cols)
    $left = 45 + $col * $panelW; $top = 80 + $row * $panelH
    $bottom = $top + $plotH
    $g.DrawString($panel.Title, $smallFont, $textBrush, $left + 125, $top - 34)
    $counts = New-Object int[] $binCount
    foreach ($item in $panel.Rows) {
        if ($null -eq $item.comment) { continue }
        $length = [int]$item.comment.Length
        $bin = [math]::Min([math]::Floor($length / 20), $binCount - 1)
        $counts[$bin]++
    }
    $maxCount = ($counts | Measure-Object -Maximum).Maximum
    if ($maxCount -lt 1) { $maxCount = 1 }
    $tick = [math]::Ceiling($maxCount / 4 / 10) * 10
    if ($tick -lt 1) { $tick = 1 }
    $yMax = $tick * 4
    for ($t = 0; $t -le 4; $t++) {
        $y = $bottom - ($t / 4 * $plotH)
        $g.DrawLine($gridPen, $left, $y, $left + $plotW, $y)
        $g.DrawString(([string]($t * $tick)), $tinyFont, $textBrush, $left - 46, $y - 10)
    }
    $g.DrawLine($axisPen, $left, $top, $left, $bottom)
    $g.DrawLine($axisPen, $left, $bottom, $left + $plotW, $bottom)
    for ($b = 0; $b -lt $binCount; $b++) {
        $barW = ($plotW / $binCount) - 2
        $x = $left + $b * ($plotW / $binCount) + 1
        $barH = $counts[$b] / $yMax * $plotH
        $y = $bottom - $barH
        $brush = New-Object System.Drawing.SolidBrush($panel.Color)
        $g.FillRectangle($brush, $x, $y, $barW, $barH)
        $brush.Dispose()
    }
    for ($t = 0; $t -le 6; $t++) {
        $value = $t * 40
        $x = $left + ($value / 260 * $plotW)
        $g.DrawString(([string]$value), $tinyFont, $textBrush, $x - 9, $bottom + 9)
    }
}
$g.DrawString('Length (characters)', $smallFont, $textBrush, 860, 925)
Save-Canvas $bmp $g 'comment_length_distribution_en.png'

# Train/validation/test distribution ----------------------------------------
$canvas = New-Canvas 1600 650
$bmp = $canvas[0]; $g = $canvas[1]
$splitPanels = @(
    @{Title='North-targeted labels'; Values=@(@(2571,184,340),@(551,40,73),@(552,39,73))},
    @{Title='South-targeted labels'; Values=@(@(2962,60,73),@(632,15,17),@(641,14,9))}
)
$splitNames = @('Train','Validation','Test')
for ($p=0; $p -lt 2; $p++) {
    $left=90+790*$p; $top=85; $w=680; $h=420; $bottom=$top+$h
    $g.DrawString($splitPanels[$p].Title,$titleFont,$textBrush,$left+185,20)
    for($t=0;$t -le 4;$t++){
        $v=$t*800; $y=$bottom-($v/3200*$h); $g.DrawLine($gridPen,$left,$y,$left+$w,$y); $g.DrawString(([string]$v),$smallFont,$textBrush,$left-62,$y-12)
    }
    $g.DrawLine($axisPen,$left,$top,$left,$bottom); $g.DrawLine($axisPen,$left,$bottom,$left+$w,$bottom)
    for($s=0;$s -lt 3;$s++){
        $center=$left+125+$s*215
        for($j=0;$j -lt 3;$j++){
            $val=$splitPanels[$p].Values[$s][$j]; $barW=48; $x=$center-78+$j*55; $barH=$val/3200*$h; $y=$bottom-$barH
            $brush=New-Object System.Drawing.SolidBrush($seriesColors[$j]); $g.FillRectangle($brush,$x,$y,$barW,$barH); $brush.Dispose()
            $valueText=[string]$val; $valueSize=$g.MeasureString($valueText,$tinyFont)
            $g.DrawString($valueText,$tinyFont,$textBrush,$x+($barW-$valueSize.Width)/2,$y-24)
        }
        $sz=$g.MeasureString($splitNames[$s],$smallFont); $g.DrawString($splitNames[$s],$smallFont,$textBrush,$center-$sz.Width/2,$bottom+18)
    }
}
for($j=0;$j -lt 3;$j++){
    $x=560+$j*190; $brush=New-Object System.Drawing.SolidBrush($seriesColors[$j]); $g.FillRectangle($brush,$x,565,25,17); $brush.Dispose(); $g.DrawString($labels[$j],$smallFont,$textBrush,$x+32,558)
}
Save-Canvas $bmp $g 'split_distribution_en.png'

# Model comparison -----------------------------------------------------------
$canvas = New-Canvas 1700 720
$bmp = $canvas[0]; $g = $canvas[1]
$models=@('PhoBERT','BiLSTM + Attn.','Random Forest','Multinomial NB','Logistic Reg.')
$north=@(0.6861,0.5586,0.5327,0.5511,0.4491)
$south=@(0.5956,0.4562,0.4492,0.3728,0.3377)
$mean=@(0.6409,0.5074,0.4909,0.4619,0.3934)
$left=105; $top=80; $w=1500; $h=480; $bottom=$top+$h
for($t=0;$t -le 4;$t++){ $v=$t*0.2; $y=$bottom-($v/0.8*$h); $g.DrawLine($gridPen,$left,$y,$left+$w,$y); $g.DrawString($v.ToString('0.0'),$smallFont,$textBrush,$left-55,$y-12) }
$g.DrawLine($axisPen,$left,$top,$left,$bottom); $g.DrawLine($axisPen,$left,$bottom,$left+$w,$bottom)
$sets=@($north,$south,$mean); $barColors=@($seriesColors[0],$seriesColors[1],$seriesColors[2]); $legend=@('North macro-F1','South macro-F1','Mean macro-F1')
for($i=0;$i -lt 5;$i++){
    $center=$left+165+$i*290
    for($j=0;$j -lt 3;$j++){
        $val=$sets[$j][$i]; $barW=62; $x=$center-105+$j*72; $barH=$val/0.8*$h; $y=$bottom-$barH
        $brush=New-Object System.Drawing.SolidBrush($barColors[$j]); $g.FillRectangle($brush,$x,$y,$barW,$barH); $brush.Dispose()
    }
    $sz=$g.MeasureString($models[$i],$smallFont); $g.DrawString($models[$i],$smallFont,$textBrush,$center-$sz.Width/2,$bottom+18)
}
for($j=0;$j -lt 3;$j++){
    $x=870+$j*265; $brush=New-Object System.Drawing.SolidBrush($barColors[$j]); $g.FillRectangle($brush,$x,25,28,18); $brush.Dispose(); $g.DrawString($legend[$j],$smallFont,$textBrush,$x+36,20)
}
$g.DrawString('Macro-F1',$smallFont,$textBrush,8,290)
Save-Canvas $bmp $g 'model_macro_f1_en.png'

# PhoBERT confusion matrices -------------------------------------------------
$canvas = New-Canvas 1600 690
$bmp = $canvas[0]; $g = $canvas[1]
$cms=@(
    @(@(508,29,15),@(21,18,0),@(18,4,51)),
    @(@(641,0,0),@(14,0,0),@(3,0,6))
)
$panelTitles=@('North-targeted','South-targeted')
$shortLabels=@('NON_HATE','PREJ.','HOSTILE')
for($p=0;$p -lt 2;$p++){
    $x0=170+790*$p; $y0=105; $cell=145
    $g.DrawString($panelTitles[$p],$titleFont,$textBrush,$x0+120,35)
    for($r=0;$r -lt 3;$r++){
        $rowTotal=($cms[$p][$r] | Measure-Object -Sum).Sum
        for($c=0;$c -lt 3;$c++){
            $ratio=if($rowTotal -gt 0){$cms[$p][$r][$c]/$rowTotal}else{0}; $shade=[int](245-175*$ratio)
            $color=[System.Drawing.Color]::FromArgb($shade,[Math]::Min(248,$shade+12),255)
            $brush=New-Object System.Drawing.SolidBrush($color); $g.FillRectangle($brush,$x0+$c*$cell,$y0+$r*$cell,$cell,$cell); $brush.Dispose()
            $g.DrawRectangle($gridPen,$x0+$c*$cell,$y0+$r*$cell,$cell,$cell)
            $s=[string]$cms[$p][$r][$c]; $sz=$g.MeasureString($s,$valueFont); $g.DrawString($s,$valueFont,$textBrush,$x0+$c*$cell+($cell-$sz.Width)/2,$y0+$r*$cell+52)
        }
        $sz=$g.MeasureString($labels[$r],$smallFont); $g.DrawString($labels[$r],$smallFont,$textBrush,$x0-$sz.Width-18,$y0+$r*$cell+55)
        $sz=$g.MeasureString($shortLabels[$r],$smallFont); $g.DrawString($shortLabels[$r],$smallFont,$textBrush,$x0+$r*$cell+($cell-$sz.Width)/2,$y0+3*$cell+15)
    }
    $g.DrawString('Predicted label',$smallFont,$textBrush,$x0+145,$y0+3*$cell+60)
}
Save-Canvas $bmp $g 'phobert_confusion_matrices_en.png'

$axisPen.Dispose(); $gridPen.Dispose(); $font.Dispose(); $smallFont.Dispose(); $tinyFont.Dispose(); $titleFont.Dispose(); $valueFont.Dispose()
