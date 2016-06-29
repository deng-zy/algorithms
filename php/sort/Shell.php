<?php
require('AbstractSort.php');
class Shell extends AbstractSort
{
	public static function sort(array $input)
	{
		$length = count($input);
		$segment = 1;
		while ($segment < $length / 3)
			$segment = 3 * $segment + 1;

		while ($segment >= 1) {
			for ($i = $segment; $i < $length; $i++) {
				// echo sprintf("%d-%d", $segment, $i), PHP_EOL;
				for ($j = $i; $j >= $segment; $j -= $segment) {
					// echo sprintf("%d-%d", $i, $j), PHP_EOL;
					if ($input[$j] < $input[$j - $segment]) {
						$tmp = $input[$j];
						$input[$j] = $input[$j - $segment];
						$input[$j - $segment] = $tmp; 
					}
				}

			}

			$segment = $segment / 3;
		}
		return $input;
	}
}
