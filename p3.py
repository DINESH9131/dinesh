def moveTower(height,fromPolt,withPole):
	if height>=1:
		moveTower(height-1,fromPole,withPole,toPole)
		moveDisk(fromPole,toPle)
		moveToewr(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
	print("moving disk from",fp,"to",tp)
moveTower(3,"A","B","C")
