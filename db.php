<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "floricultura";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Erron na conexão: " . $conn->connect_error);
}
?>