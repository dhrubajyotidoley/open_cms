<!-- Sidebar Menu Items - These collapse to the responsive navigation menu on small screens -->
            <div class="collapse navbar-collapse navbar-ex1-collapse">
                <ul class="nav navbar-nav side-nav">
                    <li class="active">
                        <a href="dashboard.php"><i class="fa fa-fw fa-dashboard"></i> Dashboard</a>
                    </li>
                    <li>
                        <a href="form_builder.php"><i class="fa fa-fw fa-file-code"></i> Form Builder</a>
                    </li>
<?php
$data_p = mysql_query("SELECT * FROM menu");
$k=1;

while($info = mysql_fetch_array( $data_p ))
{
	$name = substr($info['name'], 0, -4);
	$name=ucfirst($name);
	echo '<li>
                        <a href="'.$info['name'].'"><i class="fa fa-fw file-code"></i>'.$name.'</a>
                    </li>';
	}
?>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
