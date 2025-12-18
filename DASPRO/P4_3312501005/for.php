<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Galeri</title>
        <style>
            .container{
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
            }
            .box {
                display: flex;
                flex-direction: column;
                width: 300px;
                height: 150px;
                background-color: red;
                color: white;
            }
        </style>
        <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    </head>
    <body>
        <div class="container">
        <?php 
        for ($i = 1; $i <= 100; $i++) {
            if($i % 2 == 0) {
                echo "<div class='box animate__animated animate__bounce' style='background-color: orange'> Foto $i </div>";
            }
            else {
                echo "<div class='box animate__animated animate__bounce' style='background-color: green'> Foto $i </div>";
            }
         }
        ?>
        </div>
    </body>
    </html>

