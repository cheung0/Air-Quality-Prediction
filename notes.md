I try to use a mixture of the scientific method and art in improving my model.

# Geohash doesn't seem to improve model
!pip install geohash2
import geohash2
from sklearn.preprocessing import LabelEncoder

# Encode the coordinates into geohash
df['geohash'] = df.apply(lambda row: geohash2.encode(row['SITE_LATITUDE'], row['SITE_LONGITUDE']), axis=1)

# Perform label encoding on the 'geohash' column
label_encoder = LabelEncoder()
df['geohash'] = label_encoder.fit_transform(df['geohash'])
