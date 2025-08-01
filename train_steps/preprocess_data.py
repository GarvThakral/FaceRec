class TripletModel(tf.keras.model):
    def __init__(self,embedding_model,alpha = 0.2):
        self.model = embedding_model
        self.alpha = 0.2
    def train_step