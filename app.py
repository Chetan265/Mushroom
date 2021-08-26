from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('mushroom.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
   

        cap_shape = request.form['cap_shape']
        if (cap_shape == 'conical'):
            cap_shape_c = 1
            cap_shape_f = 0
            cap_shape_k = 0
            cap_shape_s = 0
            cap_shape_x = 0
            cap_shape_b = 0
        elif (cap_shape == 'flat'):
            cap_shape_c = 0
            cap_shape_f = 1
            cap_shape_k = 0
            cap_shape_s = 0
            cap_shape_x = 0
            cap_shape_b = 0
        elif (cap_shape == 'knobbed'):
            cap_shape_c = 0
            cap_shape_f = 0
            cap_shape_k = 1
            cap_shape_s = 0
            cap_shape_x = 0
            cap_shape_b = 0
        elif (cap_shape == 'sunken'):
            cap_shape_c = 0
            cap_shape_f = 0
            cap_shape_k = 0
            cap_shape_s = 1
            cap_shape_x = 0
            cap_shape_b = 0
        elif (cap_shape == 'convex'):
            cap_shape_c = 0
            cap_shape_f = 0
            cap_shape_k = 0
            cap_shape_s = 0
            cap_shape_x = 1
            cap_shape_b = 0
        else:
            cap_shape_c = 0
            cap_shape_f = 0
            cap_shape_k = 0
            cap_shape_s = 0
            cap_shape_x = 0
            cap_shape_b = 1
            
            
        cap_surface = request.form['cap_surface']
        if (cap_surface == 'grooves'):
            cap_surface_g = 1
            cap_surface_s = 0
            cap_surface_y = 0
            cap_surface_f = 0
        elif (cap_surface == 'smooth'):
            cap_surface_g = 0
            cap_surface_s = 1
            cap_surface_y = 0
            cap_surface_f = 0
        elif (cap_surface == 'scaly'):
            cap_surface_g = 0
            cap_surface_s = 0
            cap_surface_y = 1
            cap_surface_f = 0
        else:
            cap_surface_g = 0
            cap_surface_s = 0
            cap_surface_y = 0
            cap_surface_f = 1
            
            
        cap_color = request.form['cap_color']
        if(cap_color == "cinnamon"):
            cap_color_c = 1
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "red"):
            cap_color_c = 0
            cap_color_e = 1
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "gray"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 1
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "brown"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 1
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "pink"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 1
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "green"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 1
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "purple"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 1
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "white"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 1
            cap_color_y = 0
            cap_color_b = 0
        elif(cap_color == "yellow"):
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 1
            cap_color_b = 0
        else:
            cap_color_c = 0
            cap_color_e = 0
            cap_color_g = 0
            cap_color_n = 0
            cap_color_p = 0
            cap_color_r = 0
            cap_color_u = 0
            cap_color_w = 0
            cap_color_y = 0
            cap_color_b = 1
        
        bruises = request.form['bruises']
        if(bruises == "true"):
            bruises_t = 1
            bruises_f = 0
        else:
            bruises_t = 0
            bruises_f = 1
            
        odor = request.form['odor']
        if(odor == "creosote"):
            odor_c = 1
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "foul"):
            odor_c = 0
            odor_f = 1
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "anise"):
            odor_c = 0
            odor_f = 0
            odor_l = 1
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "musty"):
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 1
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "none"):
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 1
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "pungent"):
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 1
            odor_s = 0
            odor_y = 0
            odor_a = 0
        elif(odor == "spicy"):
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 1
            odor_y = 0
            odor_a = 0
        elif(odor == "fishy"):
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 1
            odor_a = 0
        else:
            odor_c = 0
            odor_f = 0
            odor_l = 0
            odor_m = 0
            odor_n = 0
            odor_p = 0
            odor_s = 0
            odor_y = 0
            odor_a = 1

        gill_attachment = request.form['gill_attachment']
        if (gill_attachment == 'free'):
            gill_attachment_f = 1
            gill_attachment_a = 0
        else:
            gill_attachment_f = 0
            gill_attachment_a = 1
            
        gill_spacing = request.form['gill_spacing']
        if (gill_spacing == 'crowded'):
            gill_spacing_w = 1
            gill_spacing_c = 0
        else:
            gill_spacing_w = 0
            gill_spacing_c = 1
    
        gill_size = request.form['gill_size']
        if (gill_size == 'narrow'):
            gill_size_n = 1
            gill_size_b = 0
        else:
            gill_size_n = 0
            gill_size_b = 1
            
        gill_color = request.form['gill_color']
        if (gill_color == 'red'):
            gill_color_e = 1
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'gray'):
            gill_color_e = 0
            gill_color_g = 1
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'chocolate'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 1
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'black'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 1
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'brown'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 1
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'orange'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 1
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'pink'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 1
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'green'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 1
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'purple'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 1
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'white'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 1
            gill_color_y = 0
            gill_color_b = 0
        elif (gill_color == 'yellow'):
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 1
            gill_color_b = 0
        else:
            gill_color_e = 0
            gill_color_g = 0
            gill_color_h = 0
            gill_color_k = 0
            gill_color_n = 0
            gill_color_o = 0
            gill_color_p = 0
            gill_color_r = 0
            gill_color_u = 0
            gill_color_w = 0
            gill_color_y = 0
            gill_color_b = 1
            
        stalk_shape = request.form['stalk_shape']
        if (stalk_shape == 'tapering'):
            stalk_shape_t = 1
            stalk_shape_e = 0
        else:
            stalk_shape_t = 0
            stalk_shape_e = 1
            
        stalk_root = request.form['stalk_root']
        if (stalk_root == 'missing'):        
            stalk_root_m = 1
            stalk_root_c = 0
            stalk_root_e = 0
            stalk_root_r = 0
            stalk_root_b = 0
        elif (stalk_root == 'club'):        
            stalk_root_m = 0
            stalk_root_c = 1
            stalk_root_e = 0
            stalk_root_r = 0
            stalk_root_b = 0
        elif (stalk_root == 'equal'):        
            stalk_root_m = 0
            stalk_root_c = 0
            stalk_root_e = 1
            stalk_root_r = 0
            stalk_root_b = 0
        elif (stalk_root == 'rooted'):        
            stalk_root_m = 0
            stalk_root_c = 0
            stalk_root_e = 0
            stalk_root_r = 1
            stalk_root_b = 0
        else:
            stalk_root_m = 0
            stalk_root_c = 0
            stalk_root_e = 0
            stalk_root_r = 0
            stalk_root_b = 1
            
        
        stalk_surface_above_ring = request.form['stalk_surface_above_ring']
        if (stalk_surface_above_ring == 'silky'):        
            stalk_surface_above_ring_k = 1
            stalk_surface_above_ring_s = 0
            stalk_surface_above_ring_y = 0
            stalk_surface_above_ring_f = 0
        elif (stalk_surface_above_ring == 'smooth'):        
            stalk_surface_above_ring_k = 0
            stalk_surface_above_ring_s = 1
            stalk_surface_above_ring_y = 0
            stalk_surface_above_ring_f = 0
        elif (stalk_surface_above_ring == 'scaly'):        
            stalk_surface_above_ring_k = 0
            stalk_surface_above_ring_s = 0
            stalk_surface_above_ring_y = 1
            stalk_surface_above_ring_f = 0
        else:
            stalk_surface_above_ring_k = 0
            stalk_surface_above_ring_s = 0
            stalk_surface_above_ring_y = 0
            stalk_surface_above_ring_f = 1    

        stalk_surface_below_ring = request.form['stalk_surface_below_ring']
        if (stalk_surface_below_ring == 'silky'):        
            stalk_surface_below_ring_k = 1
            stalk_surface_below_ring_s = 0
            stalk_surface_below_ring_y = 0
            stalk_surface_below_ring_f = 0
        elif (stalk_surface_below_ring == 'smooth'):        
            stalk_surface_below_ring_k = 0
            stalk_surface_below_ring_s = 1
            stalk_surface_below_ring_y = 0
            stalk_surface_below_ring_f = 0
        elif (stalk_surface_below_ring == 'scaly'):        
            stalk_surface_below_ring_k = 0
            stalk_surface_below_ring_s = 0
            stalk_surface_below_ring_y = 1
            stalk_surface_below_ring_f = 0
        else:
            stalk_surface_below_ring_k = 0
            stalk_surface_below_ring_s = 0
            stalk_surface_below_ring_y = 0
            stalk_surface_below_ring_f = 1  

        stalk_color_above_ring = request.form['stalk_color_above_ring']
        if (stalk_color_above_ring == 'cinnamon'):  
            stalk_color_above_ring_c = 1
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'red'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 1
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'gray'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 1
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'brown'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 1
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'orange'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 1
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'pink'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 1
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'white'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 1
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 0
        elif (stalk_color_above_ring == 'yellow'):  
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 1
            stalk_color_above_ring_b = 0
        else:
            stalk_color_above_ring_c = 0
            stalk_color_above_ring_e = 0
            stalk_color_above_ring_g = 0
            stalk_color_above_ring_n = 0
            stalk_color_above_ring_o = 0
            stalk_color_above_ring_p = 0
            stalk_color_above_ring_w = 0
            stalk_color_above_ring_y = 0
            stalk_color_above_ring_b = 1
       
        stalk_color_below_ring = request.form['stalk_color_below_ring']
        if (stalk_color_below_ring == 'cinnamon'):  
            stalk_color_below_ring_c = 1
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'red'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 1
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'gray'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 1
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'brown'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 1
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'orange'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 1
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'pink'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 1
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'white'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 1
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 0
        elif (stalk_color_below_ring == 'yellow'):  
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 1
            stalk_color_below_ring_b = 0
        else:
            stalk_color_below_ring_c = 0
            stalk_color_below_ring_e = 0
            stalk_color_below_ring_g = 0
            stalk_color_below_ring_n = 0
            stalk_color_below_ring_o = 0
            stalk_color_below_ring_p = 0
            stalk_color_below_ring_w = 0
            stalk_color_below_ring_y = 0
            stalk_color_below_ring_b = 1
            
        veil_color = request.form['veil_color']
        if (veil_color == 'orange'):
            veil_color_o = 1
            veil_color_w = 0
            veil_color_y = 0
            veil_color_n = 0
        elif (veil_color == 'white'):
            veil_color_o = 0
            veil_color_w = 1
            veil_color_y = 0
            veil_color_n = 0
        elif (veil_color == 'yellow'):
            veil_color_o = 0
            veil_color_w = 0
            veil_color_y = 1
            veil_color_n = 0
        else:
            veil_color_o = 0
            veil_color_w = 0
            veil_color_y = 0
            veil_color_n = 1
            
        ring_number = request.form['ring_number']
        if (ring_number == 'one'):
            ring_number_o = 1
            ring_number_t = 0
            ring_number_n = 0
        elif (ring_number == 'two'):
            ring_number_o = 0
            ring_number_t = 1
            ring_number_n = 0
        else:
            ring_number_o = 0
            ring_number_t = 0
            ring_number_n = 1

        ring_type = request.form['ring_type']
        if (ring_type == 'flaring'):
            ring_type_f = 1
            ring_type_l = 0
            ring_type_n = 0
            ring_type_p = 0
            ring_type_e = 0
        elif (ring_type == 'large'):
            ring_type_f = 0
            ring_type_l = 1
            ring_type_n = 0
            ring_type_p = 0
            ring_type_e = 0
        elif (ring_type == 'none'):
            ring_type_f = 0
            ring_type_l = 0
            ring_type_n = 1
            ring_type_p = 0
            ring_type_e = 0
        elif (ring_type == 'pendant'):
            ring_type_f = 0
            ring_type_l = 0
            ring_type_n = 0
            ring_type_p = 1
            ring_type_e = 0
        else:
            ring_type_f = 0
            ring_type_l = 0
            ring_type_n = 0
            ring_type_p = 0
            ring_type_e = 1

        spore_print_color = request.form['spore_print_color']
        if (spore_print_color == 'Chocolate'):
            spore_print_color_h = 1
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'black'):
            spore_print_color_h = 0
            spore_print_color_k = 1
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'brown'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 1
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'orange'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 1
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'green'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 1
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'purple'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 1
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'white'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 1
            spore_print_color_y = 0
            spore_print_color_b = 0
        elif (spore_print_color == 'yellow'):
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 1
            spore_print_color_b = 0
        else:
            spore_print_color_h = 0
            spore_print_color_k = 0
            spore_print_color_n = 0
            spore_print_color_o = 0
            spore_print_color_r = 0
            spore_print_color_u = 0
            spore_print_color_w = 0
            spore_print_color_y = 0
            spore_print_color_b = 1

        population = request.form['population']
        if (population == 'clustered'):
            population_c = 1
            population_n = 0
            population_s = 0
            population_v = 0
            population_y = 0
            population_a = 0
        elif (population == 'numerous'):
            population_c = 0
            population_n = 1
            population_s = 0
            population_v = 0
            population_y = 0
            population_a = 0
        elif (population == 'scattered'):
            population_c = 0
            population_n = 0
            population_s = 1
            population_v = 0
            population_y = 0
            population_a = 0
        elif (population == 'several'):
            population_c = 0
            population_n = 0
            population_s = 0
            population_v = 1
            population_y = 0
            population_a = 0            
        elif (population == 'solitary'):
            population_c = 0
            population_n = 0
            population_s = 0
            population_v = 0
            population_y = 1
            population_a = 0             
        else:
            population_c = 0
            population_n = 0
            population_s = 0
            population_v = 0
            population_y = 0
            population_a = 1  

        habitat = request.form['habitat']
        if (habitat == 'grasses'):
            habitat_g = 1
            habitat_l = 0
            habitat_m = 0
            habitat_p = 0
            habitat_u = 0
            habitat_w = 0
            habitat_d = 0
        elif (habitat == 'leaves'):
            habitat_g = 0
            habitat_l = 1
            habitat_m = 0
            habitat_p = 0
            habitat_u = 0
            habitat_w = 0
            habitat_d = 0           
        elif (habitat == 'meadows'):
            habitat_g = 0
            habitat_l = 0
            habitat_m = 1
            habitat_p = 0
            habitat_u = 0
            habitat_w = 0
            habitat_d = 0
        elif (habitat == 'paths'):
            habitat_g = 0
            habitat_l = 0
            habitat_m = 0
            habitat_p = 1
            habitat_u = 0
            habitat_w = 0
            habitat_d = 0
        elif (habitat == 'urban'):
            habitat_g = 0
            habitat_l = 0
            habitat_m = 0
            habitat_p = 0
            habitat_u = 1
            habitat_w = 0
            habitat_d = 0           
        elif (habitat == 'waste'):
            habitat_g = 0
            habitat_l = 0
            habitat_m = 0
            habitat_p = 0
            habitat_u = 0
            habitat_w = 1
            habitat_d = 0
        else:
            habitat_g = 0
            habitat_l = 0
            habitat_m = 0
            habitat_p = 0
            habitat_u = 0
            habitat_w = 0
            habitat_d = 1
            
            
        text = np.array([[cap_shape_c,cap_shape_f,cap_shape_k,cap_shape_s,cap_shape_x,
                            cap_surface_g,cap_surface_s,cap_surface_y,cap_color_c,
                            cap_color_e,cap_color_g,cap_color_n,cap_color_p,cap_color_r,cap_color_u,
                            cap_color_w,cap_color_y,bruises_t,odor_c,odor_f,
                            odor_l,odor_m,odor_n,odor_p,odor_s,odor_y,gill_attachment_f,gill_spacing_w,
                            gill_size_n,gill_color_e,
                            gill_color_g,gill_color_h,gill_color_k,gill_color_n,gill_color_o,gill_color_p,
                            gill_color_r,gill_color_u,gill_color_w,gill_color_y,stalk_shape_t,
                            stalk_root_c,stalk_root_e,stalk_root_m,stalk_root_r,
                            stalk_surface_above_ring_k,stalk_surface_above_ring_s,stalk_surface_above_ring_y,
                            stalk_surface_below_ring_k,stalk_surface_below_ring_s,
                            stalk_surface_below_ring_y,stalk_color_above_ring_c,
                            stalk_color_above_ring_e,stalk_color_above_ring_g,stalk_color_above_ring_n,
                            stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_w,
                            stalk_color_above_ring_y,stalk_color_below_ring_c,
                            stalk_color_below_ring_e,stalk_color_below_ring_g,stalk_color_below_ring_n,
                            stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_w,
                            stalk_color_below_ring_y,veil_color_o,veil_color_w,
                            veil_color_y,ring_number_o,ring_number_t,ring_type_f,
                            ring_type_l,ring_type_n,ring_type_p,spore_print_color_h,spore_print_color_k,
                            spore_print_color_n,spore_print_color_o,spore_print_color_r,spore_print_color_u,
                            spore_print_color_w,spore_print_color_y,population_c,
                            population_n,population_s,population_v,population_y,habitat_g,
                            habitat_l,habitat_m,habitat_p,habitat_u,habitat_w]])
        prediction = model.predict(text)
        if prediction == 1:
            label = 'Poissnous'
        else:
            label = 'edible'

        return render_template('index.html', prediction_text='Mushroom is {}'.format(label))





if __name__ == "__main__":
    app.run(debug=True)
