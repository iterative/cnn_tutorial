import matplotlib.pyplot as plt
import pickle
import conf
import os

with open(os.path.join(conf.data_dir, 'history.p'), 'rb') as fd:
  hist = pickle.load(fd)

acc = hist['acc']
val_acc = hist['val_acc']
loss = hist['loss']
val_loss = hist['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.savefig(os.path.join(conf.data_dir, 'plot_acc.jpeg'))
plt.close()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.savefig(os.path.join(conf.data_dir, 'plot_loss.jpeg'))
plt.close()

