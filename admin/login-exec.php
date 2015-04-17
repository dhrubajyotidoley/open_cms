<?php
include_once("../include/config.php");
connectDB();
?>
<?php
	session_start();
	
	$errmsg_arr = array();
	
	$errflag = false;
		
	function clean($str) {
		$str = @trim($str);
		if(get_magic_quotes_gpc()) {
			$str = stripslashes($str);
		}
		return mysql_real_escape_string($str);
	}
	
	$login = clean($_POST['uname']);
	$password = clean($_POST['password']);
	
	if($login == '') {
		$errmsg_arr[] = 'Login ID missing';
		$errflag = true;
	}
	if($password == '') {
		$errmsg_arr[] = 'Password missing';
		$errflag = true;
	}
	
	if($errflag) {
		$_SESSION['ERRMSG_ARR'] = $errmsg_arr;
		session_write_close();
		header("location: ../index.php");
		exit();
	}
	
	$qry="SELECT * FROM users_admin WHERE user_id='$login' AND password='".md5($password)."'";
	$result=mysql_query($qry);
	
	if($result) {
		if(mysql_num_rows($result) == 1) {
			session_regenerate_id();
			$member = mysql_fetch_assoc($result);
			$_SESSION['ADMIN_ID'] = $member['id'];
			$_SESSION['ADMIN_NAME'] = $member['name'];
			session_write_close();
			header("location: dashboard.php");
			exit();
		}else {
	
			header("location: ../index.php?er=2");
			exit();
		}
	}else {
		die("Query failed");
	}
?>
