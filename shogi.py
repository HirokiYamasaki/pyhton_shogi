King = 1
Gold = 2
Silver = 3
Knight = 4
Lance = 5
Pown = 6
Rook = 7
Bishop = 8
proSilver = 30
proKnight = 40
proLance = 50
proPown = 60
Doragon = 70
House = 80

Ally = set([King,Gold,Silver,Knight,Lance,Pown,Rook,Bishop,proSilver,proKnight,proLance,proPown,Doragon,House])
#print(Ally)

EnemyKing = 100
EnemyGold = 200
EnemySilver = 300
EnemyKnight = 400
EnemyLance = 500
EnemyPown = 600
EnemyRook = 700
EnemyBishop = 800
EnemyproSilver = 3000
EnemyproKnight = 4000
EnemyproLance = 5000
EnemyproPown = 6000
EnemyDoragon = 7000
EnemyHouse = 8000

Enemy = set([EnemyKing,EnemyGold,EnemySilver,EnemyKnight,EnemyLance,EnemyPown,EnemyRook,EnemyBishop,EnemyproSilver,EnemyproKnight,EnemyproLance,EnemyproPown,EnemyDoragon,EnemyHouse])
#print(Enemy)

tekijin = []
for i in range(3):
	for j in range(9):
		tekijin.append((i,j))
#print(tekijin)

one_two_dan = []
for i in range(2):
	for j in range(9):
		one_two_dan.append((i,j))
#print(Knight_promotion)       

one_dan = []
for i in range(1):
	for j in range(9):
		one_dan.append((i,j))
#print(Lance_promotion)

six_eight_dan = []
for i in range(6,9):
	for j in range(9):
		six_eight_dan.append((i,j))
#print(six_eight_dan)

eight_dan = []
for i in range(8,9):
	for j in range(9):
		eight_dan.append((i,j))
#print(eight_dan)

seven_eight_dan = []
for i in range(7,9):
	for j in range(9):
		seven_eight_dan.append((i,j))
#print(seven_eight_dan)



piece_can_move = []
two_Pown = []


##############################################################################
##############################################################################
class SyougiGame (object):
	def __init__(self):
		self.cells = [[None for i in range(9)]for j in range(9)]
		self.cells[8][4] = King
		self.cells[8][3] = Gold
		self.cells[8][5] = Gold
		self.cells[8][2] = Silver
		self.cells[8][6] = Silver
		self.cells[8][1] = Knight
		self.cells[8][7] = Knight
		self.cells[8][0] = Lance
		self.cells[8][8] = Lance
		self.cells[7][1] = Bishop
		self.cells[7][7] = Rook
		for i in range(9):
			self.cells[6][i] = Pown
		
		self.cells[0][4] = EnemyKing
		self.cells[0][3] = EnemyGold
		self.cells[0][5] = EnemyGold
		self.cells[0][2] = EnemySilver
		self.cells[0][6] = EnemySilver
		self.cells[0][1] = EnemyKnight
		self.cells[0][7] = EnemyKnight
		self.cells[0][0] = EnemyLance
		self.cells[0][8] = EnemyLance
		self.cells[1][7] = EnemyBishop
		self.cells[1][1] = EnemyRook
		for i in range(9):
			self.cells[2][i] = EnemyPown
			
		
		self.S_motigoma = []
		self.G_motigoma = []
		
		
##############################################################################

	###盤面と持ち駒の表示###
	def showborad(self):
		print("=" * 50)
		print("",end="     ")
		for i in range(9):
			print(str(i),end="    ")
		print("\t")
		print("",end="  ")
		print("-" * 46)
	
	
		x = 0
		for i in self.cells:
			print(str(x) + " |",end="")
			x += 1
			for j in i:
				if j == None:
					print("    ",end="")
				elif j == King:
					print("  K ",end="")
				elif j == Gold:
					print("  G ",end="")
				elif j == Silver:
					print("  S ",end="")
				elif j == Knight:
					print("  N ",end="")
				elif j == Lance:
					print("  L ",end="")
				elif j == Bishop:
					print("  B ",end="")
				elif j == Rook:
					print("  R ",end="")
				elif j == Pown:
					print("  P ",end="")
				elif j == proSilver:
					print(" pS ",end="")
				elif j == proKnight:
					print(" pN ",end="")
				elif j == proLance:
					print(" pL ",end="")
				elif j == proPown:
					print(" pP ",end="")
				elif j == Doragon:
					print("  D ",end="")
				elif j == House:
					print("  H ",end="")
	
				elif j == EnemyKing:
					print(" ^K ",end="")
				elif j == EnemyGold:
					print(" ^G ",end="")
				elif j == EnemySilver:
					print(" ^S ",end="")
				elif j == EnemyKnight:
					print(" ^N ",end="")
				elif j == EnemyLance:
					print(" ^L ",end="")
				elif j == EnemyPown:
					print(" ^P ",end="")
				elif j == EnemyRook:
					print(" ^R ",end="")
				elif j == EnemyBishop:
					print(" ^B ",end="")
				elif j == EnemyproSilver:
					print("^pS ",end="")
				elif j == EnemyproKnight:
					print("^pN ",end="")
				elif j == EnemyproLance:
					print("^pL ",end="")
				elif j == EnemyproPown:
					print("^pP ",end="")
				elif j == EnemyDoragon:
					print(" ^D ",end="")
				elif j == EnemyHouse:
					print(" ^H ",end="")
	
				print("|",end="")
			print("\t")
			print("  ",end="")
			print("-" * 46)  
	
	
	
	
		S_koma = []
		for i in self.S_motigoma:
			if i == Pown:
				S_koma.append('P')
			elif i == Lance:
				S_koma.append("L")
			elif i == Knight:
				S_koma.append("N")
			elif i == Silver:
				S_koma.append("S")
			elif i == Gold:
				S_koma.append("G")
			elif i == Bishop:
				S_koma.append("B")
			elif i == Rook:
				S_koma.append("R")
	
		#print(S_koma)
		P_cnt = S_koma.count("P")
		L_cnt = S_koma.count("L")
		N_cnt = S_koma.count("N")
		S_cnt = S_koma.count("S")
		G_cnt = S_koma.count("G")
		B_cnt = S_koma.count("B")
		R_cnt = S_koma.count("R")
		#print(P_cnt,L_cnt,N_cnt,S_cnt,G_cnt,B_cnt,R_cnt)
	
		buried1 = "先手持ち駒[Px{} , Lx{} , Nx{} , Sx{} , Gx{} , Bx{} , Rx{}]".format(P_cnt,L_cnt,N_cnt,S_cnt,G_cnt,B_cnt,R_cnt)
		
		print(buried1)
	
	
		G_koma = []
		for i in self.G_motigoma:
			if i == Pown:
				G_koma.append("P")
			elif i == Lance:
				G_koma.append("L")
			elif i == Knight:
				G_koma.append("N")
			elif i == Silver:
				G_koma.append("S")
			elif i == Gold:
				G_koma.append("G")
			elif i == Bishop:
				G_koma.append("B")
			elif i == Rook:
				G_koma.append("R")
	
		P_cnt = G_koma.count("P")
		L_cnt = G_koma.count("L")
		N_cnt = G_koma.count("N")
		S_cnt = G_koma.count("S")
		G_cnt = G_koma.count("G")
		B_cnt = G_koma.count("B")
		R_cnt = G_koma.count("R")
	
		buried2 = "後手持ち駒[Px{} , Lx{} , Nx{} , Sx{} , Gx{} , Bx{} , Rx{}]".format(P_cnt,L_cnt,N_cnt,S_cnt,G_cnt,B_cnt,R_cnt)
		print(buried2)
		
#############################################################################

	def error_flg(self):
		while True:

			input_masu = input("動かしたい駒の座標を指定してください")

			if input_masu == 'P':
				return input_masu
			elif input_masu == 'L':
				return input_masu
			elif input_masu == 'N':
				return input_masu
			elif input_masu == 'S':
				return input_masu
			elif input_masu == 'G':
				return input_masu
			elif input_masu == 'R':
				return input_masu
			elif input_masu == 'B':
				return input_masu
			

			if input_masu.isdigit() == True:      #数字が入力されている場合
				if len(input_masu) == 2:             #入力された数値の長さが2の場合
					if "9" not in input_masu:           #9が入力されていな場合
						break
					else:
						print("[エラー]升目の座標を指定してください")
				else:
					print("[エラー]升目の座標を指定してください")
			else:                           #文字が入力されている場合
					
					print("[エラー]升目の数字を入力してください")

		return input_masu
		
############################################################################

	def error_flg2(self):
		while True:
			input_num = input("リストのインデックスを指定してください")
			if input_num.isdigit() == True:
				if 0 <= int(input_num) < len(piece_can_move):
					break
				else:
					print("ng2")
			else:
				print("ng1")

		return input_num
		
#############################################################################

	###持ち駒を打つ位置を決める関数###
	def error_flg3(self):
		while True:
			input_masu3 = input('どこに打つか座標を指定して下さい')
			masu3 = input_masu3
			#print(masu3)
		
			if input_masu3.isdigit() == True:      #数字が入力されている場合
				if len(input_masu3) == 2:             #入力された数値の長さが2の場合
					if "9" not in input_masu3:           #9が入力されていな場合
						if self.cells[int(masu3[0])][int(masu3[1])] == None:
							break
						else:
							print('そこには置けません')
					else:
						print("[エラー]升目の座標を指定してください")
				else:
					print("[エラー]升目の座標を指定してください")
			else:                           #文字が入力されている場合
				print("[エラー]升目の数字を入力してください")


		return input_masu3
			
		
#############################################################################

	def yes_or_no(self):
		while True:
			input_sel = input("成りますか？")
			if input_sel == "yes":
				return 'yes'
			elif input_sel == 'no':
				return 'no'
			else:
				print('yesかnoを入力してください')
		
#############################################################################		


#############################################################################	
		
	###後手の駒を取ったとき###
	def Enemy_kakutoku(self,num):
		if self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyPown:
			self.S_motigoma.append(Pown)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyLance:
			self.S_motigoma.append(Lance)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyKnight:
			self.S_motigoma.append(Knight)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemySilver:
			self.S_motigoma.append(Silver)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyGold:
			self.S_motigoma.append(Gold)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyBishop:
			self.S_motigoma.append(Bishop)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyRook:
			self.S_motigoma.append(Rook)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyproPown:
			self.S_motigoma.append(Pown)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyproLance:
			self.S_motigoma.append(Lance)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyproKnight:
			self.S_motigoma.append(Knight)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyproSilver:
			self.S_motigoma.append(Silver)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyDoragon:
			self.S_motigoma.append(Rook)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyHouse:
			self.S_motigoma.append(Bishop)
			
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == EnemyKing:
			self.S_motigoma.append(King)

###########################################################################	


	def King_move(self):
		x = self.x
		y = self.y
		King_DIR = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
		
		for i,j in King_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
				
	
		return piece_can_move
		
#########################################################################
		
	def Rook_move(self):
		x = self.x
		y = self.y
		Rook_DIR = [(0,-1),(-1,0),(1,0),(0,1)]
			
		for RD in Rook_DIR:
				
			depth = 0
			while depth <= 10:
				depth += 1
				rx = x + (RD[0] * depth)
				ry = y + (RD[1] * depth)
					
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Ally:
						break
					elif self.cells[rx][ry] in Enemy:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
					
		return piece_can_move
		
###########################################################################

	###先手の角の動き###
	def Bishop_move(self):
		x = self.x
		y = self.y
		Bishop_DIR = [(-1,-1),(-1,1),(1,-1),(1,1)]
		
		for BD in Bishop_DIR:
			
			depth = 0
			while depth <= 10:
				depth += 1
				rx = x + (BD[0] * depth)
				ry = y + (BD[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Ally:
						break
					elif self.cells[rx][ry] in Enemy:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					break
		
		return piece_can_move
		
##########################################################################

	###先手の金の動き###
	def Gold_move(self):
		x = self.x
		y = self.y
		Gold_DIR = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0)]
		
		for i,j in Gold_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move
		
###########################################################################

	###先手の銀の動き###
	def Silver_move(self):
		x = self.x
		y = self.y
		Silver_DIR = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,1)]
		
		for i,j in Silver_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move
		
###########################################################################

	###先手の桂馬の動き###
	def Knight_move(self):
		x = self.x
		y = self.y
		Knight_DIR = [(-2,-1),(-2,1)]
		
		for i,j in Knight_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move
		
#############################################################################

	###先手の香車の動き###
	def Lance_move(self):
		x = self.x
		y = self.y
		Lance_DIR = [-1,0]		#香車の動ける方向を指定
		
		depth = 0
		while True:		#探査
			depth += 1
			
			rx = x + (Lance_DIR[0] * depth)
			ry = y + (Lance_DIR[1] * depth)
			
			if 0 <= rx < 9:			#盤の中にある時
				if self.cells[rx][ry] in Ally:		#味方の駒に当たったとき
					#print('stop')
					break
				elif self.cells[rx][ry] in Enemy:		#敵の駒に当たったとき
					piece_can_move.append((rx,ry))
					break
					
				else:
					piece_can_move.append((rx,ry))
			else:
				break
		
		return piece_can_move
		
##########################################################################

	###先手の歩の動き###
	def Pown_move(self):
		x = self.x
		y = self.y
		Pown_DIR = [-1,0]
		
		rx = Pown_DIR[0] + x
		ry = Pown_DIR[1] + y
		
		if 0 <= rx < 9 and 0 <= ry < 9:
			
			if self.cells[rx][ry] in Ally:
				pass
			else:
				piece_can_move.append((rx,ry))
		
		return piece_can_move
		
#############################################################################

	###先手の竜の動き###
	def Doragon_move(self):
		x = self.x
		y = self.y
		Doragon_DIR1 = [(0,-1),(-1,0),(1,0),(0,1)]
		Doragon_DIR2 = [(-1,-1),(-1,1),(1,-1),(1,1)]
		
		for DD1 in Doragon_DIR1:
			
			depth = 0
			while depth <= 8:
				depth += 1
				rx = x + (DD1[0] * depth)
				ry = y + (DD1[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Ally:
						break
					elif self.cells[rx][ry] in Enemy:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					continue
					
		for DD2 in Doragon_DIR2:
			
			rx = x + DD2[0]
			ry = y + DD2[1]
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
					
		return piece_can_move
		
############################################################################

	###先手の馬の動き###
	def House_move(self):
		x = self.x
		y = self.y
		House_DIR1 = [(-1,-1),(-1,1),(1,-1),(1,1)]
		House_DIR2 = [(0,-1),(-1,0),(1,0),(0,1)]
		
		for HD1 in House_DIR1:
			
			depth = 0
			while depth <= 10:
				depth += 1
				rx = x + (HD1[0] * depth)
				ry = y + (HD1[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Ally:
						break
					elif self.cells[rx][ry] in Enemy:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					break
					
		for HD2 in House_DIR2:
			
			rx = x + HD2[0]
			ry = y + HD2[1]
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Ally:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue		
									
		return piece_can_move
		
		
#####################################################################						
										
	##先手の動かす駒を指定する###					
	def Ally_catch_piece(self):
		while True:
			CP = self.error_flg()
			
			if CP == 'P':
				#print('p')
				return 'P'
			elif CP == 'L':
				#print('l')
				return 'L'
			elif CP == 'N':
				#print('n')
				return 'N'
			elif CP == 'S':
				#print('s')
				return 'S'
			elif CP == 'G':
				#print('g')
				return 'G'
			elif CP == 'B':
				#print('b')
				return 'B'
			elif CP == 'R':
				#print('r')
				return 'R'
								
				
			else:
				self.x = int(CP[0])
				self.y = int(CP[1])
				#print(self.x,self.y)
		
				if self.cells[self.x][self.y] == None:
					print('駒がありません')
					continue
					
				elif self.cells[self.x][self.y] in Enemy:
					print('[エラー]敵の駒です')
					continue
				
				elif self.cells[self.x][self.y] == King:
					CM = self.King_move()
					
				elif self.cells[self.x][self.y] == Rook:
					CM = self.Rook_move()
					#print(CM)
					
				elif self.cells[self.x][self.y] == Bishop:
					CM = self.Bishop_move()
					
				elif self.cells[self.x][self.y] == Gold:
					CM = self.Gold_move()
					
				elif self.cells[self.x][self.y] == Silver:
					CM = self.Silver_move()
				
				elif self.cells[self.x][self.y] == Knight:
					CM = self.Knight_move()
					
				elif self.cells[self.x][self.y] == Lance:
					CM = self.Lance_move()
					
				elif self.cells[self.x][self.y] == Pown:
					CM = self.Pown_move()
					
				elif self.cells[self.x][self.y] == Doragon:
					CM = self.Doragon_move()
					
				elif self.cells[self.x][self.y] == House:
					CM = self.House_move()
					
				elif self.cells[self.x][self.y] == proSilver:
					CM = self.Gold_move()
				
				elif self.cells[self.x][self.y] == proKnight:
					CM = self.Gold_move()
					
				elif self.cells[self.x][self.y] == proLance:
					CM = self.Gold_move()
					
				elif self.cells[self.x][self.y] == proPown:
					CM = self.Gold_move()
					
				
				if CM == []:
					print('その駒は動かせません')
					continue
				else:
					print(CM)
					
					
				return self.cells[self.x][self.y]
		
#############################################################################

	###先手の指定した駒を動かす###
	def Ally_move_piece(self):
		while True:
			CM = self.Ally_catch_piece()
			#print(CM)
			
			###持ち駒を打つ###
			
			if CM == 'P':
				if Pown in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					##ニ歩判定##
					#print((masu3[0],masu3[1]))
					for i in range(9):
						#print(i,int(masu3[1]))
						#print(self.cells[i][int(masu3[1])])
						two_Pown.append(self.cells[i][int(masu3[1])])
					#print(two_Pown)
					
					if Pown not in two_Pown:
						if ((int(masu3[0]),int(masu3[1]))) not in one_dan:
							self.cells[int(masu3[0])][int(masu3[1])] = Pown
							self.S_motigoma.remove(Pown)
							break
						else:
						
							print('ng2')
					else:
						print('ニ歩です')
				else:
					print('Pは持ち駒にありません')
					
			elif CM == 'L':
				if Lance in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					if ((int(masu3[0]),int(masu3[1]))) not in one_dan:
						self.cells[int(masu3[0])][int(masu3[1])] = Lance
						self.S_motigoma.remove(Lance)
						break
					else:
						print('ng2')
				else:
					print('ng')
					
			elif CM == 'N':
				if Knight in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					if ((int(masu3[0]),int(masu3[1]))) not in one_two_dan:
						self.cells[int(masu3[0])][int(masu3[1])] = Knight
						self.S_motigoma.remove(Knight)
						break
					else:
						print('ng2')
				else:
					print('ng')
					
			elif CM == 'S':
				if Silver in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Silver
					self.S_motigoma.remove(Silver)
					break
				else:
					print('ng')
					
			elif CM == 'G':
				if Gold in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Gold
					self.S_motigoma.remove(Gold)
					break
				else:
					print('ng')
					
			elif CM == 'R':
				if Rook in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Rook
					self.S_motigoma.remove(Rook)
					break
				else:
					print('ng')
					
			elif CM == 'B':
				if Bishop in self.S_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Bishop
					self.S_motigoma.remove(Bishop)
					break
					
				else:
					print('ng')		
			
			
			###盤上の駒を移動###
			else:
				input_num = self.error_flg2()
				num = int(input_num)
				#print(num)
				
				self.Enemy_kakutoku(num)
				
				if CM == King:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = King
				
				
				elif CM == Rook:
					#成るか成らないの判断
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Doragon
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Rook
								
					elif (self.x,self.y) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Doragon
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Rook
						
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Rook
						
				
				elif CM == Bishop:
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = House
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Bishop
								
					elif (self.x,self.y) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = House
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Bishop
						
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Bishop
				
				
				elif CM == Gold:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Gold
					
					
				elif CM == Silver:
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proSilver
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Silver
					elif (self.x,self.y) in tekijin:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proSilver
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Silver
						
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Silver
					
					
				elif CM == Knight:
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						if (piece_can_move[num][0],piece_can_move[num][1]) in one_two_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proKnight
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proKnight
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Knight
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Knight
						
						
				elif CM == Lance:
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						if (piece_can_move[num][0],piece_can_move[num][1]) in one_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proLance
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proLance
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Lance
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Lance
						
						
				elif CM == Pown:
					if (piece_can_move[num][0],piece_can_move[num][1]) in tekijin:
						if (piece_can_move[num][0],piece_can_move[num][1]) in one_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proPown
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proPown
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Pown
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Pown
						
						
				elif CM == Doragon:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = Doragon
					
				elif CM == House:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = House
				
				elif CM == proSilver:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proSilver
					
				elif CM == proKnight:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proKnight
					
				elif CM == proLance:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proLance
					
				elif CM == proPown:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = proPown			
				
				
				self.cells[self.x][self.y] = None
				break

##############################################################################
##############################################################################		

	###先手の駒を取ったとき
	def Ally_kakutoku(self,num):
		if self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Pown:
			self.G_motigoma.append(Pown)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Lance:
			self.G_motigoma.append(Lance)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Knight:
			self.G_motigoma.append(Knight)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Silver:
			self.G_motigoma.append(Silver)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Gold:
			self.G_motigoma.append(Gold)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Bishop:
			self.G_motigoma.append(Bishop)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Rook:
			self.G_motigoma.append(Rook)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == proPown:
			self.G_motigoma.append(Pown)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == proLance:
			self.G_motigoma.append(Lance)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == proKnight:
			self.G_motigoma.append(Knight)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == proSilver:
			self.G_motigoma.append(Silver)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == Doragon:
			self.G_motigoma.append(Rook)
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == House:
			self.G_motigoma.append(Bishop)
			
		elif self.cells[piece_can_move[num][0]][piece_can_move[num][1]] == King:
			self.G_motigoma.append(King)
			
###########################################################################	

###後手の玉の動き###
	def EnemyKing_move(self):
		x = self.x
		y = self.y
		King_DIR = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
		
		for i,j in King_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
				
	
		return piece_can_move
		
############################################################################

	###後手の飛車の動き###
	def EnemyRook_move(self):
		x = self.x
		y = self.y
		Rook_DIR = [(0,-1),(-1,0),(1,0),(0,1)]
		
		for RD in Rook_DIR:
			
			depth = 0
			while depth <= 8:
				depth += 1
				rx = x + (RD[0] * depth)
				ry = y + (RD[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Enemy:
						break
					elif self.cells[rx][ry] in Ally:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					continue
					
		
		return piece_can_move
		
#############################################################################

	###後手の角の動き###
	def EnemyBishop_move(self):
		x = self.x
		y = self.y
		Bishop_DIR = [(-1,-1),(-1,1),(1,-1),(1,1)]
		
		for BD in Bishop_DIR:
			
			depth = 0
			while depth <= 10:
				depth += 1
				rx = x + (BD[0] * depth)
				ry = y + (BD[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Enemy:
						break
					elif self.cells[rx][ry] in Ally:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					break
		
		return piece_can_move
		
##############################################################################

	###後手の金の動き###
	def EnemyGold_move(self):
		x = self.x
		y = self.y
		EnemyGold_DIR = [(-1,0),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
		
		for i,j in EnemyGold_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move

##############################################################################

	###後手の銀の動き###
	def EnemySilver_move(self):
		x = self.x
		y = self.y
		EnemySilver_DIR = [(-1,-1),(-1,1),(1,-1),(1,0),(1,1)]
		
		for i,j in EnemySilver_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move
		
##############################################################################

	###後手の桂馬の動き###
	def EnemyKnight_move(self):
		x = self.x
		y = self.y
		EnemyKnight_DIR = [(2,-1),(2,1)]
		
		for i,j in EnemyKnight_DIR:
			rx = x + i
			ry = y + j
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
		
		return piece_can_move
		
##############################################################################

	###後手の香車の動き###
	def EnemyLance_move(self):
		x = self.x
		y = self.y
		EnemyLance_DIR = [1,0]		#香車の動ける方向を指定
		
		depth = 0
		while True:		#探査
			depth += 1
			
			rx = x + (EnemyLance_DIR[0] * depth)
			ry = y + (EnemyLance_DIR[1] * depth)
			
			if 0 <= rx < 9:			#盤の中にある時
				if self.cells[rx][ry] in Enemy:		#味方の駒に当たったとき
					#print('stop')
					break
				elif self.cells[rx][ry] in Ally:		#敵の駒に当たったとき
					piece_can_move.append((rx,ry))
					break
					
				else:
					piece_can_move.append((rx,ry))
			else:
				break
		
		return piece_can_move
		
##############################################################################

	###後手の歩の動き###
	def EnemyPown_move(self):
		x = self.x
		y = self.y
		Pown_DIR = [1,0]
		
		rx = Pown_DIR[0] + x
		ry = Pown_DIR[1] + y
		
		if 0 <= rx < 9 and 0 <= ry < 9:
			
			if self.cells[rx][ry] in Enemy:
				pass
			else:
				piece_can_move.append((rx,ry))
		
		return piece_can_move
		
#############################################################################

	###先手の竜の動き###
	def EnemyDoragon_move(self):
		x = self.x
		y = self.y
		Doragon_DIR1 = [(0,-1),(-1,0),(1,0),(0,1)]
		Doragon_DIR2 = [(-1,-1),(-1,1),(1,-1),(1,1)]
		
		for DD1 in Doragon_DIR1:
			
			depth = 0
			while depth <= 8:
				depth += 1
				rx = x + (DD1[0] * depth)
				ry = y + (DD1[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Enemy:
						break
					elif self.cells[rx][ry] in Ally:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					continue
					
		for DD2 in Doragon_DIR2:
			
			rx = x + DD2[0]
			ry = y + DD2[1]
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue
					
		return piece_can_move
		
############################################################################

	###先手の馬の動き###
	def EnemyHouse_move(self):
		x = self.x
		y = self.y
		House_DIR1 = [(-1,-1),(-1,1),(1,-1),(1,1)]
		House_DIR2 = [(0,-1),(-1,0),(1,0),(0,1)]
		
		for HD1 in House_DIR1:
			
			depth = 0
			while depth <= 10:
				depth += 1
				rx = x + (HD1[0] * depth)
				ry = y + (HD1[1] * depth)
				
				if 0 <= rx < 9 and 0 <= ry < 9:
					if self.cells[rx][ry] in Enemy:
						break
					elif self.cells[rx][ry] in Ally:
						piece_can_move.append((rx,ry))
						break
					else:
						piece_can_move.append((rx,ry))
				else:
					break
					
		for HD2 in House_DIR2:
			
			rx = x + HD2[0]
			ry = y + HD2[1]
			
			if 0 <= rx < 9 and 0 <= ry < 9:
				if self.cells[rx][ry] in Enemy:
					continue
				else:
					piece_can_move.append((rx,ry))
			else:
				continue		
									
		return piece_can_move
		
		
###########################################################################			
										
		



##############################################################################
	###後手の動かす駒を指定する###
	def Enemy_catch_piece(self):
		while True:
			CP = self.error_flg()
			
			if CP == 'P':
				#print('p')
				return 'P'
			elif CP == 'L':
				#print('l')
				return 'L'
			elif CP == 'N':
				#print('n')
				return 'N'
			elif CP == 'S':
				#print('s')
				return 'S'
			elif CP == 'G':
				#print('g')
				return 'G'
			elif CP == 'B':
				#print('b')
				return 'B'
			elif CP == 'R':
				#print('r')
				return 'R'
					
				
			else:
				self.x = int(CP[0])
				self.y = int(CP[1])
				#print(self.x,self.y)
		
				if self.cells[self.x][self.y] == None:
					print('駒がありません')
					continue
					
				elif self.cells[self.x][self.y] in Ally:
					print('[エラー]敵の駒です')
					continue
				
				elif self.cells[self.x][self.y] == EnemyKing:
					CM = self.EnemyKing_move()
					
				elif self.cells[self.x][self.y] == EnemyRook:
					CM = self.EnemyRook_move()
					
				elif self.cells[self.x][self.y] == EnemyBishop:
					CM = self.EnemyBishop_move()
					
				elif self.cells[self.x][self.y] == EnemyGold:
					CM = self.EnemyGold_move()
					
				elif self.cells[self.x][self.y] == EnemySilver:
					CM = self.EnemySilver_move()
				
				elif self.cells[self.x][self.y] == EnemyKnight:
					CM = self.EnemyKnight_move()
					
				elif self.cells[self.x][self.y] == EnemyLance:
					CM = self.EnemyLance_move()
					
				elif self.cells[self.x][self.y] == EnemyPown:
					CM = self.EnemyPown_move()
					
				elif self.cells[self.x][self.y] == EnemyDoragon:
					CM = self.EnemyDoragon_move()
					
				elif self.cells[self.x][self.y] == EnemyHouse:
					CM = self.EnemyHouse_move()
					
				elif self.cells[self.x][self.y] == EnemyproSilver:
					CM = self.EnemyGold_move()
				
				elif self.cells[self.x][self.y] == EnemyproKnight:
					CM = self.EnemyGold_move()
					
				elif self.cells[self.x][self.y] == EnemyproLance:
					CM = self.EnemyGold_move()
					
				elif self.cells[self.x][self.y] == EnemyproPown:
					CM = self.EnemyGold_move()
					
				
				if CM == []:
					print('その駒は動かせません')
					continue
				else:
					print(CM)
					
					
				return self.cells[self.x][self.y]

##############################################################################
	
	###後手の指定した駒を動かす###
	def Enemy_move_piece(self):
		while True:
			CM = self.Enemy_catch_piece()
			#print(CM)
			
			if CM == 'P':
					if Pown in self.G_motigoma:
						input_masu3 = self.error_flg3()
						masu3 = input_masu3
						##ニ歩判定##
						#print((masu3[0],masu3[1]))
						for i in range(9):
							#print(i,int(masu3[1]))
							#print(self.cells[i][int(masu3[1])])
							two_Pown.append(self.cells[i][int(masu3[1])])
						#print(two_Pown)
					
						if Pown not in two_Pown:
							if ((int(masu3[0]),int(masu3[1]))) not in eight_dan:
								self.cells[int(masu3[0])][int(masu3[1])] = Pown
								self.G_motigoma.remove(Pown)
								break
							else:
								print('ng2')
						else:
							print('ニ歩です')
					else:
						print('Pは持ち駒にありません')
						
			elif CM == 'L':
				if Lance in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					if ((int(masu3[0]),int(masu3[1]))) not in one_dan:
						self.cells[int(masu3[0])][int(masu3[1])] = Lance
						self.G_motigoma.remove(Lance)
						break
					else:
						print('ng2')
				else:
					print('ng')
					
			elif CM == 'N':
				if Knight in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					if ((int(masu3[0]),int(masu3[1]))) not in one_two_dan:
						self.cells[int(masu3[0])][int(masu3[1])] = Knight
						self.G_motigoma.remove(Knight)
						break
					else:
						print('ng2')
				else:
					print('ng')
					
			elif CM == 'S':
				if Silver in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Silver
					self.G_motigoma.remove(Silver)
					break
				else:
					print('ng')
					
			elif CM == 'G':
				if Gold in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Gold
					self.G_motigoma.remove(Gold)
					break
				else:
					print('ng')
					
			elif CM == 'R':
				if Rook in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Rook
					self.G_motigoma.remove(Rook)
					break
				else:
					print('ng')
					
			elif CM == 'B':
				if Bishop in self.G_motigoma:
					input_masu3 = self.error_flg3()
					masu3 = input_masu3
					self.cells[int(masu3[0])][int(masu3[1])] = Bishop
					self.G_motigoma.remove(Bishop)
					break
					
				else:
					print('ng')		
		
			
			
			else:
				input_num = self.error_flg2()
				num = int(input_num)
				#print(num)
				
				self.Ally_kakutoku(num)
						
				if CM == EnemyKing:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyKing
					
						
						
				elif CM == EnemyRook:
					#成るか成らないの判断
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyDoragon
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyRook
										
					elif ((self.x,self.y)) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyDoragon
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyRook
								
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyRook
								
						
				elif CM == EnemyBishop:
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyHouse
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyBishop
										
					elif (self.x,self.y) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyHouse
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyBishop
								
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyBishop
						
						
				elif CM == EnemyGold:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyGold
							
							
				elif CM == EnemySilver:
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproSilver
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemySilver
					elif (self.x,self.y) in six_eight_dan:
						YN = self.yes_or_no()
						if YN == 'yes':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproSilver
						elif YN == 'no':
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemySilver
								
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemySilver
							
							
				elif CM == EnemyKnight:
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						if (piece_can_move[num][0],piece_can_move[num][1]) in seven_eight_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproKnight
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproKnight
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyKnight
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyKnight
								
								
				elif CM == EnemyLance:
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						if (piece_can_move[num][0],piece_can_move[num][1]) in eight_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproLance
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproLance
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyLance
					else:
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyLance
								
								
				elif CM == EnemyPown:
					if (piece_can_move[num][0],piece_can_move[num][1]) in six_eight_dan:
						if (piece_can_move[num][0],piece_can_move[num][1]) in eight_dan:
							self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproPown
						else:
							YN = self.yes_or_no()
							if YN == 'yes':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproPown
							elif YN == 'no':
								self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyPown
					else:
						print('ok')
						self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyPown
								
								
				elif CM == EnemyDoragon:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyDoragon
							
				elif CM == EnemyHouse:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyHouse
						
				elif CM == EnemyproSilver:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproSilver
							
				elif CM == EnemyproKnight:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproKnight
										
				elif CM == EnemyproLance:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproLance
							
				elif CM == EnemyproPown:
					self.cells[piece_can_move[num][0]][piece_can_move[num][1]] = EnemyproPown			
						
						
				self.cells[self.x][self.y] = None
				break
				
##############################################################################

	###ゲーム終了###
	def is_finish(self):
		flg = True
		
		if King in self.S_motigoma or King in self.G_motigoma:
			flg = False
		
		return flg
		
############################################################################
			
	###勝ち負け判定###
	def result(self):
		if King in self.S_motigoma:
			print('先手の勝ちです')
		
		if King in self.G_motigoma:
			print('後手の勝ちです')

#############################################################################




###実行###
if __name__ == '__main__':
	game = SyougiGame()
	game.showborad()
	cnt = 0
	while True:
		cnt += 1
		if cnt % 2 == 0:
			print('後手の番です')
			game.Enemy_move_piece()
		elif cnt % 2 == 1 :
			print('先手の番です')
			game.Ally_move_piece()
		
		game.showborad()
		if game.is_finish() == False:
			break
		piece_can_move = []
	
	game.result()