<?php
require ("AbstractSort.php");
class Quick extends AbstractSort
{

	public static function sort(array $input)
	{
		self::_quick($input, 0, count($input) - 1);
		return $input;
	}

	private static function _quick(&$input, $left, $right)
	{
		if ($left > $right) 
			return;
	    
	    $base = $input[$left];
	    $i = $left;
	    $j = $right;

	    while ($i != $j) {
	    	while ($input[$j] >= $base && $i < $j)
	    		$j--;

	    	while ($input[$i] <= $base && $i < $j)
	    		$i++;

	    	if ($i < $j) {
	    		$tmp = $input[$i];
	    		$input[$i] = $input[$j];
	    		$input[$j] = $tmp;
	    	}
	    }

	    $input[$left] = $input[$i];
	    $input[$i] = $base;

	    self::_quick($input, $left, $i-1);
	    self::_quick($input, $i+1, $right);
	}
}
