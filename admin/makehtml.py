#!/usr/bin/env python

import MySQLdb


def Body(*arg):
    name = arg[0][0].lower()
    name = name.replace (" ", "_")
    nameplease = "'"+name+"'"
    a = len(arg[0])
    fetch = ''
    post = ''
    insert = ''
    values = ''
    update = ''
    k = 1
    while k!=a:
        try:
            n = arg[0][k].replace (" ", "_")
        except:
            n = arg[0][k]
        fetch += "$"+n+"=$q["+str(k)+"];"
        post +="$"+n+"=$_POST['"+n+"'];"
        insert +="`"+n.lower()+"`,"
        values += "'$"+n+"',"
        update += "`"+n.lower()+"`='$"+n+"',"
        k+=1
    insert = insert[:-1]
    values = values[:-1]
    update = update[:-1]
    l = len(arg)
    n = 1
    t = ''
    while n!=l:
        t += arg[n]
        n+=1
    html = '''
<?php
include("header.php");

$id=$_REQUEST['id'];

if($id!="")
{
	$q=mysql_fetch_array(mysql_query("select * from '''+name+''' where id=$id"));
	'''+fetch+'''
	
}	

if(isset($_POST['submit']))
{
  
  '''+post+'''
   
  $f1=isDuplicate($id,"id","'''+name+'''","");
  
     if(!$f1)
		{
				executeQuery("insert into '''+name+''' ('''+insert+''') values ('''+values+''')");
				echo '<script type="text/javascript">window.location = "'''+name+'_list.php'+'''";</script>';
		}
     else 
		{
				executeQuery("update '''+name+''' set '''+update+''' where id=$id");
				echo '<script type="text/javascript">window.location = "'''+name+'_list.php'+'''";</script>';
		}
}
?>

                <!-- /.row -->
                <div class="row">
                <!-- forms -->
                <div class="col-lg-1"></div>
                    <div class="col-lg-10">

                        <form name="form" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" onSubmit="return submitForm();">
<br>
'''+t+'''
    <center>
    <input type="hidden" name="id" id="id" value="<?php echo $id;?>">
<input class="form-control" name="doc_no" value="<?php echo $doc_no; ?>" type="hidden">
<input class="form-control" name="pcode" value="<?php echo $pcode; ?>" type="hidden">
<input class="form-control" name="fir" value="<?php echo $fir; ?>" type="hidden">
    <button type="submit" name="submit" class="btn btn-primary" style="margin-right: 50px;">Submit</button>
    <button type="reset" class="btn btn-danger">Reset</button>
    </center>
    <div style="height: 40px;"></div>
</form>
                    </div>
</div>
                <!-- /.row -->


<?php
include("footer.php");
?>
'''
    return html

def Text_Input(t):
    html = '''
<div class="form-group">
                                <label>'''+t.capitalize()+'''</label>
                                <input class="form-control" name="'''+t.replace (" ", "_")+'''" value="<?php echo $'''+t.replace (" ", "_")+'''; ?>" placeholder="'''+t.capitalize()+'''">
                            </div>'''
    return html

def Static():
    html = '''
<div class="form-group">
                                <label>Static Control</label>
                                <p class="form-control-static">email@example.com</p>
                            </div>'''
    return html

def Static_Title(t):
    html = '''
<div class="form-group">
                                <h2>'''+t.capitalize()+'''</h2>
                            </div>'''
    return html


def Upload_File(t):
    html = '''
<div class="form-group">
                                <label>'''+t.capitalize()+'''</label>
                                <input type="file" name="'''+t.replace (" ", "_")+'''">
                            </div>'''
    return html

def Text_Area(t):
    html = '''
<div class="form-group">
                                <label>'''+t.capitalize()+'''</label>
                                <textarea class="form-control" rows="3" name="'''+t.replace (" ", "_")+'''"><?php echo $'''+t.replace (" ", "_")+''';?></textarea>
                            </div>'''
    return html

def Check_Box(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    while n!=l:
        t += '''<div class="checkbox">
                                    <label>
                                        <input type="checkbox" name="'''+arg[0][0].replace (" ", "_")+'''" value="'''+arg[0][n]+'''">'''+arg[0][n]+'''
                                    </label>
                                </div>'''
        n+=1
    html = '''
<div class="form-group">
<label>'''+arg[0][0].capitalize()+'''</label>'''+t+'''                        
                            </div>'''
    return html


def Check_Box_Inline(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    while n!=l:
        t += '''<label class="checkbox-inline">
                                    <input type="checkbox" name="'''+arg[0][0].replace (" ", "_")+'''" value="'''+arg[0][n]+'''">'''+arg[0][n]+'''
                                </label>'''
        n+=1
    html = '''
<div class="form-group">
<label>'''+arg[0][0].capitalize()+'''</label>'''+t+'''                        
                            </div>'''
    return html

def Radio_Button(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    name = "$"+arg[0][0].replace (" ", "_")
    #value = "'"+arg[0][n]+"'"
    #logic = name + "==" +value
    while n!=l:
        t += '''<div class="radio">
                                    <label>
                                        <input type="radio" name="'''+arg[0][0].replace (" ", "_")+'''" id="optionsRadios1" value="'''+arg[0][n]+'''" <?php if('''+name+"=="+"'"+arg[0][n]+"'"''') echo checked; ?>>'''+arg[0][n]+'''
                                </label>
                                </div>'''
        n+=1
    html = '''
<div class="form-group">
                                <label>'''+arg[0][0].capitalize()+'''</label>'''+t+'''
                                    
                            </div>
'''
    return html

def Radio_Button_Inline(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    while n!=l:
        t += '''<div class="radio">
                                    <label class="radio-inline">
                                        <input type="radio" name="'''+arg[0][0].replace (" ", "_")+'''" id="optionsRadios1" value="'''+arg[0][n]+'''" >'''+arg[0][n]+'''
                                </label>
                                </div>'''
        n+=1
    html = '''
<div class="form-group">
                                <label>'''+arg[0][0].capitalize()+'''</label>'''+t+'''
                                    
                            </div>
'''
    return html

def Select(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    while n!=l:
        t += '''<option>'''+arg[0][n]+'''</option>'''
        n+=1
    html = '''
<div class="form-group">
                                <label>'''+arg[0][0].capitalize()+'''</label>
                                <select class="form-control" name='''+arg[0][0].replace (" ", "_")+'''>
                                <option>--select--</option>
                        '''+t+'''
                                </select>
                            </div>
'''
    return html

def Select_Multiple(*arg):
    l = len(arg[0])
    n = 1
    t = ''
    while n!=l:
        t += '''<option>'''+arg[0][n]+'''</option>'''
        n+=1
    html = '''
<div class="form-group">
                                <label>'''+arg[0][0].capitalize()+'''</label>
                                <select multiple class="form-control" name='''+arg[0][0].replace (" ", "_")+'''>
                        '''+t+'''
                                </select>
                            </div>
'''
    return html


def var3(t):
    a = "`"+t.lower()+"` varchar(300) NOT NULL,"
    return a

def var1(t):
    a = "`"+t.lower()+"` varchar(100) NOT NULL,"
    return a

def int1(t):
    a = "`"+t.lower()+"` int(20) NOT NULL DEFAULT '0',"
    return a

def txt(t):
    a = "`"+t.lower()+"` text NOT NULL,"
    return a


def CreateTable(name, table):
    sql = '''CREATE TABLE IF NOT EXISTS `'''+name.lower()+'''` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
'''+table+'''
  `flag` varchar(300) NOT NULL DEFAULT '0',
  `active` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
);'''
    print sql
    db = MySQLdb.connect(host="localhost", 
                     user="username", 
                      passwd="password", 
                      db="dbname")
    pro = db.cursor()
    pro.execute(sql)
    db.commit()
    db.close()

def CreateHTML(name, html):
    global create_file
    global copy_file
    create_file = '/PATH_TO_ADMIN_FOLDER/admin/f/'
    copy_file = '/PATH_TO_ADMIN_FOLDER/admin/'
    f = open(create_file+name.lower()+".php", "w")
    f.write(html)
    f.close()
    import shutil
    shutil.copy2(create_file+name.lower()+'.php', copy_file+name.lower()+'.php')

def CreateHTMLlist(name):
    lower = name.lower()
    html = '''
<?php
include("header.php");

$id=$_REQUEST['id'];

if ($_POST['hide']>=1) 
{
	$n=$_POST['hide'];
	executeQuery("delete from '''+lower+''' where id='$n'");
}
?>
<script language="javascript" type="text/javascript">
function del(a)
{
 	var x=window.confirm("Do you Want To delete this?")
	if (x)
	{
		document.getElementById('hide').value=a;
		document.form.submit();
	}
}
</script>


                <!-- Page Heading -->
                <div class="row">
                    <div class="col-lg-10">
                        <h1 class="page-header">
                            '''+name+''' List
                        </h1>
                        <ol class="breadcrumb">
                            <li>
                                <i class="fa fa-dashboard"></i>  <a href="dashboard.php">Dashboard</a>
                            </li>
                            <li class="active">
                                <i class="fa fa-edit"></i> Forms
                            </li>
                        </ol>
                    </div>
                    <div class="col-lg-2">
                    <div class="btn btn-primary"><a href="'''+name.lower()+'''.php">Add New</a></div>
                    </div>
                </div>
                <!-- /.row -->
                <div class="row">
                <!-- forms -->
                <div class="col-lg-2"></div>
                    <div class="col-lg-8">
<center>
<div class="col-xs-4" style="background-color: #336699; color: white; padding: 10px 0; height: 30px;"><b>Title</b></div>
<div class="col-xs-4" style="background-color: #336699; color: white; padding: 10px 0; height: 30px;"><b>Edit</b></div>
<div class="col-xs-4" style="background-color: #336699; color: white; padding: 10px 0; height: 30px;"><b>Delete</b></div>
</center>
<center>
<form name="form" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" onSubmit="return submitForm();">
<?php
$pagenum=$_REQUEST['pagenum'];
if (!(isset($pagenum)))
{
	$pagenum = 1;
}
				
$data = mysql_query("SELECT * FROM '''+lower+'''");
$rows = mysql_num_rows($data);
	
echo "<input  type='hidden' id='pagenum' name='pagenum' value='$pagenum'> ";
$page_rows = 20;
				
$last = ceil($rows/$page_rows);
				
if ($pagenum < 1)
{
	$pagenum = 1;
}
elseif ($pagenum > $last)
{
	$pagenum = $last;
}
$max = 'limit ' .($pagenum - 1) * $page_rows .',' .$page_rows; 

$data_p = mysql_query("SELECT * FROM '''+lower+''' $max");
$k=1;
if(!$data_p) {
			echo '<div class="col-xs-12" style="background-color: #C0C0C0; color: black; padding: 10px 0; height: 40px; border-bottom: 1px solid #336699">No Data</a></div>';		
		}
while($info = mysql_fetch_array( $data_p ))
{
?>
<div class="col-xs-4" style="background-color: #C0C0C0; color: black; padding: 10px 0; height: 40px; border-bottom: 1px solid #336699"><?php echo $info[1]; ?></div>
<div class="col-xs-4" style="background-color: #C0C0C0; color: black; padding: 10px 0; height: 40px; border-bottom: 1px solid #336699"><a href="'''+lower+'''.php?id=<?php echo $info[0]; ?>">[ Edit ]</a></div>
<div class="col-xs-4" style="background-color: #C0C0C0; color: black; padding: 10px 0; height: 40px; border-bottom: 1px solid #336699"><a title='Delete' name="del-<?php echo $info[0]?>" onclick="del(<?php echo $info[0]?>);" class='delch'><div style="font-weight: bold; color: blue; font-size: 15px;">[ X ]</div></a></div>
<?php
	$k++;	  
}
$home = HOME;
echo "<tr><td colspan='6'>&nbsp;</td></tr>
<tr><td colspan='6' align='center'>&nbsp;</td></tr>
<tr><td colspan='6' align='center'><span class='pagenav'> --&nbsp;Page $pagenum of $last&nbsp;-- </span></td></tr>
<tr><td colspan='6' align='center'>";
				
if ($pagenum == 1)
{
	echo "<span class='pagenav'><img src='images/bt_previous1.jpg' alt='FIRST' width='22' height='22' title='FIRST' border='0' /> </span>";
	echo "<span class='agenav'> <img src='images/bt_previous2.jpg' alt='PREVIOUS' width='65' height='22' title='PREVIOUS' border='0' /> </span>";
}
else
{
	echo "<span class='pagenav'><a href='{$_SERVER['PHP_SELF']}?pagenum=1'><img src='images/bt_previous1.jpg' alt='FIRST' width='22' height='22' title='FIRST' border='0' /></a> </span>";
	$previous = $pagenum-1;
	echo "<span class='pagenav'> <a href='{$_SERVER['PHP_SELF']}?pagenum=$previous'><img src='images/bt_previous2.jpg' alt='PREVIOUS' width='65' height='22' title='PREVIOUS' border='0' /></a> </span>";
}
		
echo "<span style='font-size:24px; color:#707070;'> ..... </span>";
		
if ($pagenum == $last)
{
	echo "<span class='pagenav'> <img src='images/bt_next2.jpg' alt='FIRST' width='65' height='22' title='FIRST' border='0' /> </span>";
	echo "<span class='pagenav'> <img src='images/bt_next1.jpg' alt='FIRST' width='22' height='22' title='FIRST' border='0' /></span></td></tr>";
}
else {
	$next = $pagenum+1;
	echo "<span class='pagenav'> <a href='{$_SERVER['PHP_SELF']}?pagenum=$next'><img src='images/bt_next2.jpg' alt='FIRST' width='65' height='22' title='FIRST' border='0' /></a> </span>";
	echo "<span class='pagenav'> <a href='{$_SERVER['PHP_SELF']}?pagenum=$last'><img src='images/bt_next1.jpg' alt='FIRST' width='22' height='22' title='FIRST' border='0' /></a></span></td></tr>";
}
?>

<input type="hidden" id="hide" name="hide" value="0">
<input type="hidden" name="id" id="id" value="<?php echo $id;?>">
</form>
</center>
                    </div>
</div><!-- /.row -->

<div style="height: 100px;"></div>


<?php
include("footer.php");
?>
'''
    f = open(create_file+name.lower()+"_list.php", "w")
    f.write(html)
    f.close()
    import shutil
    shutil.copy2(create_file+name.lower()+'_list.php', copy_file+name.lower()+'_list.php')
