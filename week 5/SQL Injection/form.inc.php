<?php
include_once("dbh.php");
session_start();
$username = $_POST['username'];
$password = $_POST['password'];

$sql = "SELECT * FROM users WHERE userName = '$username' AND userPassword = '$password'"; //'OR '1' = '1''
$result = $conn->query($sql);

if (mysqli_num_rows($result) > 0) {
   $_SESSION['username'] = $username;
   header('Location: admin.php?note=loginSuccess');
} else {
   header('Location: index.php?note=loginFailed');
}
