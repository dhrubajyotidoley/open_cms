<?php
include_once("../include/config.php");
include_once("../include/sqlfunctions.php");
	
	session_start();
	
	if(!isset($_SESSION['ADMIN_ID']) || (trim($_SESSION['ADMIN_ID']) == '')) {
		header("location: ../index.php?er=1");
		exit();
	} else {
		$name = $_SESSION['ADMIN_NAME'];
		}
?>
