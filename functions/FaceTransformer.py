from . import (
    torch,
    nn
)

class FaceTransformer(nn.Module):
    def __init__(self, backbone, d_model=512, nhead=8, num_layers=3):
        super(FaceTransformer, self).__init__()
        self.backbone = backbone
        self.d_model = d_model
        
        self.projection = nn.Linear(512, d_model)
        
        self.pos_encoder = nn.Parameter(torch.randn(1, 49, d_model))
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model * 49, 512)  # Final embedding size

    def forward(self, x):
        features = self.backbone.extract_features(x)
        features = torch.nn.functional.relu(features)
        
        features = features.view(features.size(0), 512, -1)
        features = self.projection(features.permute(0, 2, 1))
        
        features = features + self.pos_encoder
        
        output = self.transformer_encoder(features.permute(1, 0, 2))
        output = output.permute(1, 2, 0).flatten(1)
        return self.fc(output)