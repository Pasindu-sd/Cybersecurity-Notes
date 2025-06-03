<?php
session_start();
if (!isset($_SESSION['username'])) {
   header('Location: index.php?error=PleaseLogin');
} else {
   $username = $_SESSION['username'];
}

echo "<h1>Hello $username</h1>";
