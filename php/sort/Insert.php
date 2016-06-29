<?php
require ("AbstractSort.php");
class Insert extends AbstractSort
{
	public static function sort(array $insert)
	{
		$length = count($insert);
		for ($i=1; $i < $length; $i++) {
			for ($j=$i; $j > 0; $j--) {
				if ($insert[$j] < $insert[$j-1]) {
					$tmp = $insert[$j];
					$insert[$j] = $insert[$j - 1];
					$insert[$j - 1] = $tmp;
				}
			}
		}
		return $insert;
	}

}
