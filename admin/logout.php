<?php
	session_start();

	unset($_SESSION['ADMIN_ID']);
	unset($_SESSION['ADMIN_NAME']);
?>
<?php
header('Location: index.php');
?>
