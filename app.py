from flask import Flask, request, jsonify, send_file, send_from_directory
import json
import os

app = Flask(__name__, static_url_path='', static_folder='.')

# In-memory store for block sections (for demonstration purposes)
block_sections = []

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/block-section', methods=['POST'])
def add_block_section():
    data = request.json
    point1 = data['point1']
    point2 = data['point2']
    block_sections.append({'point1': point1, 'point2': point2})
    print(f"Block section added: {point1} to {point2}")
    return jsonify({'status': 'success', 'message': 'Block section added', 'block_sections': block_sections})

@app.route('/api/block-sections', methods=['GET'])
def get_block_sections():
    return jsonify(block_sections)

@app.route('/api/save-block-sections', methods=['GET'])
def save_block_sections():
    filename = 'block_sections.geojson'
    block_sections_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for section in block_sections:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [section['point1']['lng'], section['point1']['lat']],
                    [section['point2']['lng'], section['point2']['lat']]
                ]
            },
            "properties": {}
        }
        block_sections_geojson['features'].append(feature)

    with open(filename, 'w') as f:
        json.dump(block_sections_geojson, f)

    # Check if the file was created and log its existence
    if os.path.exists(filename):
        print(f"{filename} created successfully.")
    else:
        print(f"Failed to create {filename}.")

    return send_file(filename, as_attachment=True)

@app.route('/api/undo-block-section', methods=['POST'])
def undo_block_section():
    if block_sections:
        removed_section = block_sections.pop()
        print(f"Removed block section: {removed_section}")
    return jsonify({'status': 'success', 'message': 'Last block section removed', 'block_sections': block_sections})

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
