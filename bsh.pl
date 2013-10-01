#!/usr/bin/perl
$r=1, $i=0, $FILE='rfc5594.txt', $c=' ';
open(FILE);
foreach $l (<FILE>){
	if ($r eq 1){		
		if (length(($l =~ /( *)$/)[0]) eq 0){$b=0}
		else{$b=1}
		$r=0;
	}
	else{$b.= sprintf "%02b",length(($l =~ /( *)$/)[0])}
}

while($byte ne '00000000'){
	undef($byte);
	$byte=substr($b,$i,8);
	$i+=8;
	if($byte ne '00000000'){
		push(@text,chr(oct('0b'.$byte)));
	}
}

print reverse(@text);
