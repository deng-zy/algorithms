<?php
$dir = dirname(__FILE__);
$argv = $_SERVER['argv'];
if (empty($argv[1])) {
    echo "please input sort algorithm name", PHP_EOL;
    exit(-1);
}

$algorithmName = ucfirst($argv[1]);
$algorithmFile = sprintf("%s/sort/%s.php", $dir, $algorithmName);
if (!file_exists($algorithmFile)) {
    echo sprintf("%s not exists.%s", $algorithmFile, PHP_EOL);
    exit(-2);
}

require ($algorithmFile);

if (!class_exists($algorithmName)) {
    echo sprintf("class %s not found %s", $algorithmName, PHP_EOL);
    exit(-3);
}


$runNumber = empty($argv[2]) ? 1: (int) $argv[2];
$arrayLength = empty($argv[3]) ? 5: (int) $argv[3];
call_user_func_array([$algorithmName, 'main'], [$runNumber, $arrayLength]);