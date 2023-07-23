<?php
$registry_dir = __DIR__ . '/registry';
$user_dir = "$registry_dir/{$_POST['user']}";
$repository_dir = "$user_dir/{$_POST['repo']}.kip";

if (!is_dir($user_dir))
    mkdir("$registry_dir/{$_POST['username']}");

file_put_contents($repository_dir, $_FILES['file']);