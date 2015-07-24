COUNTER=1
while [ $COUNTER -lt 12 ] ; do 
	cat Wemo$COUNTER\Bulb14 | sed -e 's/2015.................//g' > 14tmp$COUNTER | mv 14tmp$COUNTER Wemo$COUNTER\Bulb14
	cat Wemo$COUNTER\Bulb10AND6 | sed -e 's/2015.................//g' > 10AND6tmp$COUNTER | mv 10AND6tmp$COUNTER Wemo$COUNTER\Bulb10AND6
	cat Wemo$COUNTER\Bulb10 | sed -e 's/2015.................//g' > 10tmp$COUNTER | mv 10tmp$COUNTER Wemo$COUNTER\Bulb10
	cat Wemo$COUNTER\Bulb6 | sed -e 's/2015.................//g' > 6tmp$COUNTER | mv 6tmp$COUNTER Wemo$COUNTER\Bulb6
	cat Wemo$COUNTER\Bulb14AND6 | sed -e 's/2015.................//g' > 14AND6tmp$COUNTER | mv 14AND6tmp$COUNTER Wemo$COUNTER\Bulb14AND6
        cat Wemo$COUNTER\Bulb14AND10 | sed -e 's/2015.................//g' > 14AND10tmp$COUNTER | mv 14AND10tmp$COUNTER Wemo$COUNTER\Bulb14AND10
        cat Wemo$COUNTER\Bulb14AND10AND6 | sed -e 's/2015.................//g' > 14AND10AND6tmp$COUNTER | mv 14AND10AND6tmp$COUNTER Wemo$COUNTER\Bulb14AND10AND6
	let COUNTER=$COUNTER+1
done
