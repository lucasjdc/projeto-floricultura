<?php
if (isset($_GET['i'])) {
    $i = intval($_GET['i']);
    $estoque = json_decode(file_get_contents("estoque.json"), true);

    if ($estoque[$i]['quantidade'] > 0) {
        $estoque[$i]['quantidade'] -= 1;
    }

    file_put_contents("estoque.json", json_encode($estoque, JSON_PRETTY_PRINT));   
}
header("Location: index.php");