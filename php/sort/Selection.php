<?php
require("AbstractSort.php");
class Selection extends AbstractSort
{
	public static function sort(array $input)
	{
		$length = count($input);
		for ($i = 0; $i < $length; $i++) {
			$min = $i;
			for ($j = $i + 1; $j < $length; $j++) {
				if ($input[$j] < $input[$min])
					$min = $j;
			}

			$tmp = $input[$i];
			$input[$i] = $input[$min];
			$input[$min] = $tmp;
		}
		return $input;
	}
}

Selection::main();
