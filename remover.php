<?php
if (isset($_GET['i'])) {
    $estoque = json_decode(file_get_contents("estoque.json"), true);

    array_splice($estoque, $_GET['i'], 1);

    file_put_contents("estoque.json", json_encode($estoque, JSON_PRETTY_PRINT));
}
header("Location: index.php");