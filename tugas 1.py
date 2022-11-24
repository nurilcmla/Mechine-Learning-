from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# x = Data, Y = Target
x = [[0,0], [0,1], [1,0], [1,1],[1,2],[0,2],[2,2],[2,1],[0,3],[1,3],[2,3],[3,3]]
y = [0,0,0,1,1,0,2,1,0,1,2,3]

# Training and Classify
clf = NearestCentroid()
clf.fit(x,y)

# Prediksi
print ("Logika AND Metode K. Nearest Neighbors (KNN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("0 2 = ", clf.predict([[0,2]]))
print ("2 2 = ", clf.predict([[2,2]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("0 3 = ", clf.predict([[0,3]]))
print ("1 3 = ", clf.predict([[1,3]]))
print ("2 3 = ", clf.predict([[2,3]]))
print ("3 3 = ", clf.predict([[3,3]]))
