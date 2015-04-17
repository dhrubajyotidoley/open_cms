<?php
include('header.php');
?>

<!-- REQUIRED: jquery, lodash, dust-linkedin -->
		<script src="js/libs.min.js"></script>

		<script src="js/formbuilder.min.js"></script>
		<link href="css/formbuilder.css" media="screen" rel="stylesheet" />

		<script>

			// On document ready
			$(function(){

				// IF you're loaded existing form data, it's up to you
				// how you want to load the JSON. In this example,
				// we pull it using ajax - all that form builder requires
				// is that you inject the JSON when calling `formbuilder`
				$.getJSON( 'fake-form-db-vals.json', function(resp){

          // Create an instance of form builder
					var myForm = new formbuilder({

						// Provide a dom element the form will be built to
						// jQuery or simpleDOM elements required
						targets: $('.formbuilder'),

						// A callback allowing you to handle saving the form
						save: function(formData){
							console.log(formData);
							var str_json = JSON.stringify(formData)
    						window.location = "form_python.php?save="+str_json;
						},

						// we loaded existing JSON, so we have a form_id. If you're
						// creating a new form, this may be left out
						form_id: resp.form_id,

						// we loaded existing JSON, so we pass it in here. If you're
						// creating a new form, this may be left out
						startingModel: resp.model

					});
        });
			});
		</script>
<style type="text/css">
.frmb-save {
    background-color: #428bca;
    border-color: #357ebd;
    color: #fff;
    margin-top: 1em;
}
.frmb-save {
    -moz-user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
    cursor: pointer;
    display: inline-block;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857;
    margin-bottom: 0;
    padding: 6px 12px;
    text-align: center;
    vertical-align: middle;
    white-space: nowrap;
}
.frmb-add-elem {
	margin-bottom: 1em;
}
.frmb-group {
	margin-bottom: 1em;
}
.frmb-add-elem {
	position: fixed;
	right: 0;
	margin-right: 20%;
}
.frmb-save {
	margin-left: 45%;
}
</style>
<div class="row">
                    <div class="col-lg-12">
<div class="formbuilder"></div>
</div></div>
<?php
//include('footer.php');
?>