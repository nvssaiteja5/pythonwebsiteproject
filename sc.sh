pylint $1 > result

SCORE=`cat result | grep rated|awk  '{print $7}' |awk -F/ '{print $1}'`
echo $SCORE
if [[ $SCORE > 5.00 ]]
then
echo "Success"
else 
echo "Score is $SCORE, Score must be  10"
exit 1
fi
