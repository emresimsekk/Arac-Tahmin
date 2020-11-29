import re
import pandas as pd
import numpy as np

###Verilerin Yüklenmesi
data=pd.read_csv('veri.csv')

digest=[]

###Fiyat kolonunu regexden geçirerek TL ayrıldı(12.000 TL-12.000)
for i in range(565):
    ###Regular Expression (Yorumlardaki noktalama işaretlerini değiştirme)
     comment=re.sub('[A-Z]','',data['fiyat'][i])
    ###Lower (Küçük harfe çevirme)
     comment=comment.lower()
    ###Split (Kelimeleri listeye çevirme)
     comment=comment.split()
    ###Stopword al kümeye çevir kümelerinde içinde kelime yoksa gövdesini bul 
     comment=' '.join(comment)
     digest.append(comment)
    
###Bağımsız değişkenler
X=pd.concat([data.iloc[:, 0:4],data.iloc[:,5]],axis=1)
###Bağımlı değişkenler
y=pd.DataFrame(data=digest,columns=['price'])

###Toplam eksik hücre sayısı
total=data.isnull().sum()

###Encoder ile number değerlere dönüştürüldü.
from sklearn.preprocessing import LabelEncoder 
labelencoder = LabelEncoder()

X.iloc[:, 0] = labelencoder.fit_transform(X.iloc[:, 0]) 
X.iloc[:, 3] = labelencoder.fit_transform(X.iloc[:, 3])
X.iloc[:, 4] = labelencoder.fit_transform(X.iloc[:, 4])


###Veri setinin eğitim ve test olarak bölümlenmesi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)


###Ölçekleme işlemi gerçekleştirildi.
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
###fit=eğit, transform=eğitimi uygulama kullan
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)
y_train_scale = scaler.fit_transform(y_train) 
y_test_scale = scaler.fit_transform(y_test) 


###Support Vector Machine 
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train_scale, y_train_scale)
y_pred_scale = regressor.predict(X_test_scale)


###Modelin başarı durumu 
from sklearn.metrics import r2_score
print(r2_score(y_test_scale, y_pred_scale))

