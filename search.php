<?php
require "db.php";

$query = $_GET['q'] ?? '';

$stmt = $conn->prepare(
"SELECT title, description FROM content WHERE title LIKE CONCAT('%', ?, '%')"
);

$stmt->bind_param("s",$query);
$stmt->execute();

$result = $stmt->get_result();
?>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Search Results</title>
<link rel="stylesheet" href="styles.css">
</head>

<body>

<div class="page">

<div class="header">
<div class="header-inner">
<div class="logo">Logo</div>
</div>
</div>

<div class="main">
<div class="main-inner">

<div class="nav">
<div class="nav-item">Home</div>
<div class="nav-item">About</div>
<div class="nav-item">Contact</div>
</div>

<div class="content">

<h2>Search Results for "<?php echo htmlspecialchars($query); ?>"</h2>

<?php

if($result->num_rows > 0){

while($row = $result->fetch_assoc()){

echo "<div class='content-block'>";
echo "<h3>".htmlspecialchars($row['title'])."</h3>";
echo "<p>".htmlspecialchars($row['description'])."</p>";
echo "</div>";

}

}else{

echo "<p>No results found.</p>";

}

?>

</div>
</div>
</div>

</div>

</body>
</html>