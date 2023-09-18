<?php

    $nomeAluno = $_POST['nomeAluno'];
    $anoAluno = $_POST['anoAluno'];
    $turmaAluno = $_POST['turmaAluno'];
    $dataAtestado = $_POST['dataAtestado'];
    $diasAtestado = $_POST['diasAtestado'];
    $justificativa = $_POST['justificativa'];
    $autor = $_POST['autor'];

    // DB connection

    $host = "localhost";
    $dbname = "base_atestados";
    $username = "root";
    $password = "3di@Junior";

    $conn = mysqli_connect( hostname: $host,
                            username: $username,
                            password: $password,
                            database: $dbname);

    if (mysqli_connect_errno()){
        die("Connection error: " . mysqli_connect_error());
    }

    $sql = "INSERT INTO atestados (nomeAluno, anoAluno, turmaAluno, dataAtestado, diasAtestado, justificativa, autor)
            VALUES (?, ?, ?, ?, ?, ?, ?)";

    $stmt = mysqli_stmt_init($conn);

    if ( ! mysqli_stmt_prepare($stmt, $sql)){
        die(mysqli_error($conn));
    }

    mysqli_stmt_bind_param( $stmt, "ssssiss",
                            $nomeAluno,
                            $anoAluno,
                            $turmaAluno,
                            $dataAtestado,
                            $diasAtestado,
                            $justificativa,
                            $autor);

    mysqli_stmt_execute($stmt);

    echo "Atestado Cadastrado.";


 



     /* $conn = new mysqli('localhost', 'root', '3di@Junior', 'base_atestados', '3306');
    if ($conn->connect_error) {
        die('Connection Failed: ' .$conn->connect_error);
    }else{
        $stmt = $conn->prepare("insert into base_atestados(nomeAluno, anoAluno,
        turmaAluno, dataAtestado, diasAtestado, justificativa, autor)
            values (?, ?, ?, ?, ?, ?, ?)");
            
        $stmt->bind_param("sisdtiss", $nomeAluno, $anoAluno, $turmaAluno, $dataAtestado,
        $diasAtestado,$justificativa ,$autor);
        $stmt->execute();
        echo "Justificativa registrada com sucesso"; 
        $stmt->close();
        $conn->close();
    
    } 
 */

?>