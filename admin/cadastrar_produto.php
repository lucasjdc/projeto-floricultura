<?php
session_start();
if (!isset($_SESSION['logado'])) {
    header("Location: login.php");
    exit;
}

include '../db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $preco = $_POST['preco'];
    $descricao = $_POST['descricao'];

    // Upload da imagem
    $imagem = $_FILES['imagem']['name'];
    $destino = "../uploads/" . basename($imagem);

    if (move_uploaded_file($_FILES['imagem']['tmp_name'], $destino)) {
        $sql = "INSERT INTO produtos (nome, preco, imagem, descricao) 
                VALUES ('$nome', '$preco', '$imagem', '$descricao')";
        if ($conn->query($sql) === TRUE) {
            echo "Produto cadastrado com sucesso!";
        } else {
            echo "Erro: " . $conn->error;
        }
    } else {
        echo "Erro ao enviar imagem.";
    }
}
?>

<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Cadastrar Produto</title></head>
<body>
  <h1>Novo Produto</h1>
  <form method="post" enctype="multipart/form-data">
    <input type="text" name="nome" placeholder="Nome do produto" required><br>
    <input type="text" name="preco" placeholder="Preço" required><br>
    <textarea name="descricao" placeholder="Descrição"></textarea><br>
    <input type="file" name="imagem" required><br>
    <button type="submit">Cadastrar</button>
  </form>
  <br>
  <a href="dashboard.php">Voltar</a>
</body>
</html>
