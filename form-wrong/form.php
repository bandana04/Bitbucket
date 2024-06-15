<?php
$target_dir = "uploads/";

if (!is_dir($target_dir)) {
    mkdir($target_dir, 0777, true); 
}

if(isset($_POST["submit"]) && isset($_FILES["document"])) { 
    $target_file = $target_dir. basename($_FILES["document"]["name"]);
    
    $pdfFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
    if ($pdfFileType!= "pdf") {
        echo "Only PDF files are allowed.";
        exit;
    }

    if (move_uploaded_file($_FILES["document"]["tmp_name"], $target_file)) {
        echo "Thank you. Your file is uploaded.";
    } else {
        echo "There was an error uploading your file.";
    }
} else {
    echo "Please select a file to upload.";
}
?>

<form method="POST" enctype="multipart/form-data">
Select document to upload (only pdf are allowed):
<input type="file" name="document">
<input type="submit" value="Upload Document" name="submit">
</form>