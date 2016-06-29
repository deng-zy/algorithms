<?php
abstract class AbstractSort
{
	public static function sort(array $input)
	{

	}

	public static function generationArray($length, $min=1, $max=1000)
	{
		$array = [];
		for ($i = 0; $i < $length; $i++) 
			$array[] = mt_rand($min, $max);

		return $array;
	}

	protected function toString(array $origin)
	{
		return sprintf("[%s]", implode(", ",  $origin));
	}

	public static function main($testNumber=null, $arrayLength=null)
	{
		$testNumber = empty($testNumber)? 1: $testNumber;
		$arrayLength = empty($arrayLength)? 10: $arrayLength;

		for ($i = 0; $i < $testNumber; $i++) {
			$source = static::generationArray($arrayLength);
			echo static::toString($source), "\n";

			$begin = microtime(true);
			echo static::toString(static::sort($source)), "\n";
			$end = microtime(true);
			echo sprintf("numbers: %d, %.4f", count($source), $end - $begin), "\n";
		}
	}
}