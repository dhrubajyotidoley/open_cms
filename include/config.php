<?php
/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'PASSWORD');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** MySQL Database Name */
define('DB_NAME', 'DBNAME');

define('TITLE', 'emailer :: Home');

function connectDB() {
	mysql_connect(DB_HOST,DB_USER,DB_PASSWORD) or die("could not connect database.");
	mysql_select_db(DB_NAME) or die("Could not select database");
}
function closeDB() {
	$link = mysql_connect(DB_HOST,DB_USER,DB_PASSWORD);
	mysql_close($link);
}
$dbc = @mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
?>
