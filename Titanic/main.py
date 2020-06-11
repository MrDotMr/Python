import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import warnings
import numpy as np

#读数据集
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
temp= pd.read_csv("test.csv") #保留原ID
titanic = pd.concat([train, test], sort=False) #合并训练集和测试集
len_train = train.shape[0] #训练集数据规模

# 处理缺失数据
titanic.isnull().sum()[titanic.isnull().sum() > 0] #缺失数值统计
train.Fare = train.Fare.fillna(train.Fare.mean()) #使用均值填充费用缺失值
test.Fare = test.Fare.fillna(train.Fare.mean())
train.Cabin = train.Cabin.fillna("miss") #使用miss填充仓位缺失值
test.Cabin = test.Cabin.fillna("miss")
train.Embarked = train.Embarked.fillna(train.Embarked.mode()[0])
test.Embarked = test.Embarked.fillna(train.Embarked.mode()[0])
train['title'] = train.Name.apply(lambda x: x.split('.')[0].split(',')[1].strip())
test['title'] = test.Name.apply(lambda x: x.split('.')[0].split(',')[1].strip())
newtitles = {
    "Capt": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Level": "Royalty",
    "Don": "Royalty",
    "Sir": "Royalty",
    "Dr": "Officer",
    "Rev": "Officer",
    "the Countess": "Royalty",
    "Dona": "Royalty",
    "Mme": "Mrs",
    "Mlle": "Miss",
    "Ms": "Mrs",
    "Mr": "Mr",
    "Mrs": "Mrs",
    "Miss": "Miss",
    "Master": "Master",
    "Lady": "Royalty"}
train['title'] = train.title.map(newtitles)
test['title'] = test.title.map(newtitles)
print(train.groupby(['title', 'Sex']).Age.mean()) #年龄均值

# 获取新年龄方法
def newage(cols):
    title = cols[0]
    Sex = cols[1]
    Age = cols[2]
    if pd.isnull(Age):
        if title == 'Master' and Sex == "male":
            return 5
        elif title == 'Miss' and Sex == 'female':
            return 22
        elif title == 'Mr' and Sex == 'male':
            return 32
        elif title == 'Mrs' and Sex == 'female':
            return 36
        elif title == 'Officer' and Sex == 'female':
            return 49
        elif title == 'Officer' and Sex == 'male':
            return 47
        elif title == 'Royalty' and Sex == 'female':
            return 41
        else:
            return 42
    else:
        return Age

train.Age = train[['title', 'Sex', 'Age']].apply(newage, axis=1)
test.Age = test[['title', 'Sex', 'Age']].apply(newage, axis=1)

# 可视化分析
warnings.filterwarnings(action="ignore")
plt.figure(figsize=(12,10))
plt.subplot(3, 3, 1)
sns.barplot('Pclass', 'Survived', data=train)
plt.subplot(3, 3, 2)
sns.barplot('SibSp', 'Survived', data=train)
plt.subplot(3, 3, 3)
sns.barplot('Parch', 'Survived', data=train)
plt.subplot(3, 3, 4)
sns.barplot('Sex', 'Survived', data=train)
plt.subplot(3, 3, 5)
sns.barplot('Ticket', 'Survived', data=train)
plt.subplot(3, 3, 6)
sns.barplot('Cabin', 'Survived', data=train)
plt.subplot(3, 3, 7)
sns.barplot('Embarked', 'Survived', data=train)
plt.subplot(3, 3, 8)
sns.distplot(train[train.Survived == 1].Age, color='green', kde=False)
sns.distplot(train[train.Survived == 0].Age, color='orange', kde=False)
plt.subplot(3, 3, 9)
sns.distplot(train[train.Survived == 1].Fare, color='green', kde=False)
sns.distplot(train[train.Survived == 0].Fare, color='orange', kde=False)
plt.savefig('DirectData.jpg')
plt.show()

# 特征优化与重组
train['Relatives'] = 2*train.SibSp + train.Parch
test['Relatives'] = 2*test.SibSp + test.Parch
train['Ticket2'] = train.Ticket.apply(lambda x: len(x)**2)
test['Ticket2'] = test.Ticket.apply(lambda x: len(x)**2)
train['Cabin2'] = train.Cabin.apply(lambda x: len(x)**2)
test['Cabin2'] = test.Cabin.apply(lambda x: len(x)**2)
train['Name2'] = train.Name.apply(lambda x: x.split(',')[0].strip())
test['Name2'] = test.Name.apply(lambda x: x.split(',')[0].strip())
warnings.filterwarnings(action="ignore")
plt.figure()
plt.subplot(3, 1, 1)
sns.barplot('Relatives', 'Survived', data=train)
plt.subplot(3, 1, 2)
sns.barplot('Ticket2', 'Survived', data=train)
plt.subplot(3, 1, 3)
sns.barplot('Cabin2', 'Survived', data=train)
plt.savefig('FixedData.jpg')
plt.show()

# 建模准备
train.drop(['PassengerId', 'Name', 'Ticket', 'SibSp', 'Parch', 'Cabin'], axis=1, inplace=True)
test.drop(['PassengerId', 'Name', 'Ticket', 'SibSp', 'Parch', 'Cabin'], axis=1, inplace=True)
titanic = pd.concat([train, test], sort=False)
titanic = pd.get_dummies(titanic)
train = titanic[:len_train]
test = titanic[len_train:]
train.Survived = train.Survived.astype('int')
train.Survived.dtype
xtrain = train.drop("Survived", axis=1)
ytrain = train['Survived']
xtest = test.drop("Survived", axis=1)

#SVM
svc=make_pipeline(StandardScaler(),SVC())
r=[0.0001,0.001,0.1,1,10,50,100]
PSVM=[{'svc__C':r, 'svc__kernel':['linear']},
      {'svc__C':r, 'svc__gamma':r, 'svc__kernel':['rbf']}]
GSSVM=GridSearchCV(estimator=svc, param_grid=PSVM, scoring='accuracy')
#随机森林
RF=RandomForestClassifier(random_state=1)
PRF=[{'n_estimators':[10,100],'max_depth':[3,6],'criterion':['gini','entropy']}]
GSRF=GridSearchCV(estimator=RF, param_grid=PRF, scoring='accuracy',cv=2)

#交叉验证
scores_svm=cross_val_score(GSSVM, xtrain.astype(float), ytrain,scoring='accuracy')
scores_rf=cross_val_score(GSRF,xtrain,ytrain,scoring='accuracy',cv=5)
print('SVM ',np.mean(scores_svm))
print('随机森林 ',np.mean(scores_rf))

#预测与输出结果
model=GSSVM.fit(xtrain, ytrain)
pred=model.predict(xtest)
output=pd.DataFrame({'PassengerId':temp['PassengerId'],'Survived':pred})
output.to_csv('submission.csv', index=False)
