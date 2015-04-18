<?php
require_once('auth.php');
include_once("../include/config.php");
include_once("../include/sqlfunctions.php");
connectDB();
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="OpenNirvana" >

    <title>Open CMS - <?php echo $name; ?></title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/sb-admin.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="css/plugins/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <div id="wrapper">

        <!-- Navigation -->
        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="dashboard.php">Open CMS Admin</a>
            </div>
            <!-- Top Menu Items -->
            <!-- ul class="nav navbar-right top-nav">
                
                
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> <?php echo $name; ?> <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        <li>
                            
                        </li>
                    </ul>
                </li>
            </ul -->
<style type="text/css">
.navbar-right a {
	text-decoration: none;
	color: white;
	padding: 0px 10px 0 0;
	margin-top: 10px;
}
</style>
            <div class="nav navbar-right top-nav">
            <a href="logout.php"><i class="fa fa-fw fa-power-off"></i> Log Out</a>
            </div>
<?php            
			  include('menu.php');   
?>            
        </nav>
        
        <div id="page-wrapper">

            <div class="container-fluid">
