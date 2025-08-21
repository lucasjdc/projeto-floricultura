<?php
function carregarEstoque() {
    $arquivo = __DIR__ . '/../data/estoque.json';
    if (!file_exists($arquivo)) {
        file_put_contents($arquivo, "[]");
    }
    return json_decode(file_get_contents($arquivo), true);
}

function salvarEstoque($estoque) {
    $arquivo = __DIR__ . '/../data/estoque.json';
    file_put_contents($arquivo, json_encode($estoque, JSON_PRETTY_PRINT));
}