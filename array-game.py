import numpy as np

class minimum_value_path_finder():

    def __init__(self,square_matrix_dimension=10 )  : #sqaure_matrix_dimension is the number of rows and columns for the square matrix

        self.random_matrix=np.random.permutation(np.arange(1,(square_matrix_dimension*square_matrix_dimension)+1)).reshape(square_matrix_dimension,square_matrix_dimension)

    def index_finder(self): # returns the indices of the matrices
        indices=[]
        for i,j in enumerate(self.random_matrix):
            for c,k in enumerate(j):
                indices.append([i,c])
        return indices

    def index_to_val(self,index):# returns value of a particular index
        return self.random_matrix[index[0],index[1]]

    def general_adjacent_indeces(self,pos):#general formula for finding the adjacent indices
        general_adjacent_positions=[[pos[0],pos[1]+1],[pos[0],pos[1]-1],[pos[0]-1,pos[1]],[pos[0]+1,pos[1]],[pos[0]+1,pos[1]+1],[pos[0]+1,pos[1]-1],[pos[0]-1,pos[1]+1],[pos[0]-1,pos[1]-1]]
        return general_adjacent_positions

    def specific_adjacent_indeces(self):#returns  all adjacent indices
        specific_adjacent_positions={}
        matrix_indices=self.index_finder()
        for i in matrix_indices:
            specific_adjacent_positions[str(i)]=[k for k in self.general_adjacent_indeces(i) if k in matrix_indices]
        return specific_adjacent_positions

    def minimum_adjacent_value_finder(self,pos):# returns adjacent minimum value path
        indices=self.specific_adjacent_indeces()
        path=[pos]
        for i in path:
            value_index=indices[str(path[-1])]
            value_index_dict=dict(zip([self.index_to_val(k) for k in value_index],value_index))
            min_val_index=value_index_dict[min(value_index_dict)]
            if not min_val_index in path:
                path.append(min_val_index)
            else:
                #print(value_index_dict)
                try:
                    values_excluding_path={i:v for i,v in value_index_dict.items() if v  not in path}
                    min_val_index=values_excluding_path[min(values_excluding_path)]
                    path.append(min_val_index)
                except:
                    print('All min vals used')                
        return 'indices are :'+ '-->'.join(map(str,path)),'values are :' + '-->'.join(map(str,[self.index_to_val(i) for i in path]))



path_finder=minimum_value_path_finder(square_matrix_dimension=5)
print(path_finder.minimum_adjacent_value_finder([1,1]))
