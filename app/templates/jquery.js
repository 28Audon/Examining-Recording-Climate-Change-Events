<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>load demo</title>
  <style>
  body {
    font-size: 12px;
    font-family: Arial;
  }
  </style>
  <script src="https://code.jquery.com/jquery-3.6.3.js"></script>
</head>
<body>
 
<b>Projects:</b>
<ol id="new-projects"></ol>
 
<script>
$( "#new-projects" ).load( "/resources/load.html #projects li" );
</script>
 
</body>
</html>