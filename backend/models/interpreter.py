from models.sequence_to_vector.seq2vec import SequenceToVector
from models.vector_to_class.vec2class import VectorToClass
import json

class Interpreter:
    def __init__(self) -> None:
        self.s2v: SequenceToVector = None
        self.v2c: VectorToClass = None

    def parse(self, sequence: str):
        """Processes user query and returns predicted intent."""
        print(f"🔍 Received Query: {sequence}")  # Debug Input Query
        
        if self.s2v is None or self.v2c is None:
            print("❌ Error: Model is not initialized properly.")
            return None

        # Convert text to vector
        embedding = self.s2v.get_embedding(sequence)
        print(f"📊 Generated Embedding: {embedding}")  # Debug Vector Representation
        
        # Predict intent
        predicted_class = self.v2c.get_class(embedding)
        print(f"✅ Predicted Intent: {predicted_class}")  # Debug Predicted Intent
        
        return predicted_class
    
    @staticmethod
    def create_new_interpreter(name: str):
        """Creates a new interpreter and saves it."""
        s2v = SequenceToVector()
        v2c = VectorToClass()
        s2v.initialize()
        v2c.initialize(s2v)

        model_data = {
            "s2v": s2v.to_json(),
            "v2c": v2c.to_json()
        }

        with open(f"models/saved/{name}.json", "w") as f:
            json.dump(model_data, f, indent=1)
        
        print(f"✅ New interpreter '{name}' created and saved.")

    @staticmethod
    def load_interpreter(name: str = "default_stem"):
        """Loads a saved interpreter model."""
        interpreter = Interpreter()
        try:
            with open(f"models/saved/{name}.json", "r") as _file:
                saved_model = json.load(_file)
            
            interpreter.s2v = SequenceToVector.from_json(saved_model["s2v"])
            interpreter.v2c = VectorToClass.from_json(saved_model["v2c"])
            print(f"✅ Successfully loaded interpreter: {name}")
        except FileNotFoundError:
            print(f"❌ Error: Model file 'models/saved/{name}.json' not found.")
        except KeyError as e:
            print(f"❌ Error: Missing key in model file: {e}")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

        return interpreter
