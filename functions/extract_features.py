from . import (
    Image, 
    cv2,
    FaceTransformer, 
    torch, 
    detect_face, 
    pth_processing, 
    device, 
)

pth_backbone_model = torch.jit.load('model/torchscript_model_0_66_49_wo_gl.pth').to(device)
model = FaceTransformer(pth_backbone_model).to(device)

def extract_features(image):
    """
        Extract features from a cv2 image.
        The code itself detects the face in the image and extracts the features.
    """
    face = detect_face(image)
    if face is None:
        return None
    x1, y1, x2, y2 = face
    face_img = Image.fromarray(cv2.cvtColor(image[y1:y2, x1:x2], cv2.COLOR_BGR2RGB))
    face_tensor = pth_processing(face_img)
    with torch.no_grad():
        features = model(face_tensor)
        
    return features.cpu().numpy()