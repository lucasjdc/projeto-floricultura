<?php include 'db.php'; ?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Produtos</title>
</head>
<body>
  <h1>Nossos Produtos</h1>
  <div class="produtos">
    <?php
      $sql = "SELECT * FROM produtos";
      $result = $conn->query($sql);

      if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
              echo "<div class='produto'>";
              echo "<img src='uploads/".$row['imagem']."' width='200'><br>";
              echo "<h3>".$row['nome']."</h3>";
              echo "<p>R$ ".$row['preco']."</p>";
              echo "<p>".$row['descricao']."</p>";
              echo "<a href='https://wa.me/5599999999999?text=Quero%20comprar%20".$row['nome']."'>Comprar pelo WhatsApp</a>";
              echo "</div>";
          }
      } else {
          echo "Nenhum produto disponível.";
      }
    ?>
  </div>
</body>
</html>
