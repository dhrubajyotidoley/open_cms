<?php

// Prevent caching.
header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 01 Jan 1996 00:00:00 GMT');

// The JSON standard MIME header.
header('Content-type: application/json');

// This ID parameter is sent by our javascript client.
$data = $_GET['save'];


$data = json_encode($data);
//$data = json_decode($data, true);

/*
//Complete Data printing
echo 'Chirag data ';
print_r($data);
echo ' END';
exit();
*/
//echo count($data);

//print_r ($data);

//echo j_string_decoded['model'][1];
/*
foreach($data as $users){
   foreach($users as $user){
      echo $user['label'];
      echo $user['type'];
   }
}
*/


#shell_exec('python /media/work/public_html/form_builder/admin/testme.py');

$param1 = $data;
 
$command = "/home6/opennirv/python27/Python-2.7.4/python /home6/opennirv/public_html/beta/form_builder/admin/testme.py";
$command .= " $param1 2>&1";
 
header('Content-Type: text/html; charset=utf-8');
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';
echo "<style type='text/css'>
 body{
 background:#000;
 color: #7FFF00;
 font-family:'Lucida Console',sans-serif !important;
 font-size: 12px;
 }
 </style>";
 
$pid = popen( $command,"r");
 
echo "<body><pre>";
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 echo "<script>window.scrollTo(0,99999);</script>";
 usleep(100000);
}
pclose($pid);
 
echo "</pre><script>window.scrollTo(0,99999);</script>";
echo "<br /><br />Script finalizado<br /><br />";
echo "<h1>Your form has been generated</h1>";

echo "<script type='text/javascript'>window.location = \"dashboard.php\";</script>";
?>
