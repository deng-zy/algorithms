<?php
require ("AbstractSort.php");
class Bubble extends AbstractSort
{
	public static function sort(array $input)
	{
		$length = count($input);
		for ($i = 0; $i < $length; $i++) {

			for ($j = 0; $j < $length - 1; $j++) {

				if ($input[$j] > $input[$j + 1]) {
					$tmp = $input[$j + 1];
					$input[$j + 1] = $input[$j];
					$input[$j] = $tmp;
				}
				
			}

		}

		return $input;
	}
}

Bubble::main();