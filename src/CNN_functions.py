import matplotlib.pyplot as plt

def generator(data,target,bs,rootImg,mode='train'):
    #función generadora para proporcionar datos a las CNN poco a poco
    images=[]
    labels=[]
    count=0
    while True:
        images.append(cv2.imread(rootImg+data.iloc[count]))
        if target.iloc[count] == 1:
            labels.append([0,1])
        else:
            labels.append([1,0])
        count+=1
        if len(labels)==bs:
            images=np.array(images)
            labels=np.array(labels)
            if mode == "eval":
              yield images
            else:
              yield images, labels
            images=[]
            labels=[]
        if count==data.shape[0]:
            if mode == "eval":
                break
            else:
                count=0


def plot_acc_loss(acc, val_acc, loss, val_loss):
    epochs_number = range(1, len(acc) + 1)
    # Train and validation accuracy
    plt.plot(epochs_number, acc, 'b', label='Training accuracy')
    plt.plot(epochs_number, val_acc, 'r', label='Validation accuracy')
    plt.title('Training and Validation accuracy')
    plt.legend()
    plt.figure()
    # Train and validation loss
    plt.plot(epochs_number, loss, 'b', label='Training loss')
    plt.plot(epochs_number, val_loss, 'r', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()
    plt.show()

def conf_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    # Visualiamos la matriz de confusión
    cm_df = pd.DataFrame(cm)  
    plt.figure(figsize = (7,5))  
    sn.heatmap(cm_df, annot=True, annot_kws={"size": 12}, fmt="d", xticklabels =["MSI","MSS"], yticklabels=["MSI","MSS"]) # font size  
    plt.yticks(rotation=0) 
    plt.show() 
    