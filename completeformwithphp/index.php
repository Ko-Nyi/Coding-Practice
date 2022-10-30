<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Getting Personal information</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <p>Personal Information</p>
    <?php
    $nameerr=$parenterr=$birthdayerr=$ageerr=$educationerr=" ";
    $name=$parent=$birthday=$age=$education=" ";

    if ($_SERVER["REQUEST_METHOD"]=="POST"){
        if (empty($_POST["name"])){
            $nameerr="Name is required";
        }else{
            $name=test_input($_POST["name"]);
        }

        if (empty($_POST["parent"])){
            $parenterr="Parents name is required";
        }else{
            $parent=test_input($_POST["parent"]);
        }

        if (empty($_POST["birthday"])){
            $birthdayerr="Birthday is required";
        }else{
            $birthday=test_input($_POST["birthday"]);
        }

        if(empty($_POST["age"])){
            $ageerr="Age is requied";
        }else{
            $age=test_input($_POST["age"]);
        }

        if (empty($_POST["education"])){
            $educationerr="Education is required";
        }else{
            $education=test_input($_POST["education"]);
        }
    }

    function test_input($data){
        $data=trim($data);
        $data=stripslashes($data);
        $data=htmlspecialchars($data);
        return $data;
    }

    ?>
    <p><span class="error">* required field</span></p>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        Name: <input type="text" name="name">
        <span class="error">*<?php echo $nameerr; ?></span>
        <br><br>

        Parents: <input type="text" name="parent">
        <span class="error">* <?php echo $parenterr; ?> </span>
        <br><br>

        Birthday: <input type="date" name="birthday">
        <span class="error">* <?php echo $birthdayerr; ?> </span>
        <br><br>

        Age: <input type="number" name="age">
        <span class="error">* <?php echo $ageerr; ?> </span>
        <br><br>

        Education: 
        <input type="radio" name="education" value="High School" >High School
        <input type="radio" name="education" value="Graduated">Graduated
        <input type="radio" name="education" value="Primary School">Primary School
        <input type="radio" name="education" value="University">University
        <span class="error">* <?php echo $educationerr;?> </span>
        <br><br>
        <input type="submit" name="submit" value="submit">
</form>
<?php
echo "<h2> Your Input: </h2>";
echo "Name:  $name";
echo "<br>";
echo  "Parents:  $parent";
echo "<br>";
echo "Birthday:  $birthday";
echo "<br>";
echo "Age:  $age";
echo "<br>";
echo "Education:  $education Student";
?>
</body>
</html>