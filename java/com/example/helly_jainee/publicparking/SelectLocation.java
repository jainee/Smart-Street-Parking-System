package com.example.helly_jainee.publicparking;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.NavigationView;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.Spinner;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.json.JSONArray;

import java.util.ArrayList;
import java.util.Map;

public class SelectLocation extends Fragment {

    private RecyclerView recyclerView;
    private ArrayList<Item> arrayList;
    Button btngo;
    public static String selectedloc;
    FirebaseDatabase database;
    DatabaseReference myRef;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.select_location,null);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        RelativeLayout relativeLayout = view.findViewById(R.id.rldisplay);
        database = FirebaseDatabase.getInstance();
        final ArrayList<String> values = new ArrayList<String>();
        values.add("Select Location");
        myRef = database.getReference();
        myRef.addValueEventListener(new ValueEventListener() {

            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                for ( DataSnapshot child : dataSnapshot.getChildren())
                {
                    Log.d("TAG", "Value is: " + child.getKey());
                    values.add(child.getKey());
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });

        final Spinner locations = (Spinner) view.findViewById(R.id.spinner);
        ArrayAdapter<String> loc = new ArrayAdapter<String>(this.getContext(),
                android.R.layout.simple_list_item_1, values);
        loc.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        locations.setAdapter(loc);

        btngo = (Button) view.findViewById(R.id.btngo);
        btngo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(locations.getSelectedItemPosition()!=0) {
                    selectedloc = locations.getSelectedItem().toString();
                    openDisplaySlotsActivity();
                    /*myRef = database.getReference("lpsv");
                    myRef.addValueEventListener(new ValueEventListener() {

                        @Override
                        public void onDataChange(DataSnapshot dataSnapshot) {
                            long total = dataSnapshot.getChildrenCount();
                            Map<String, Object> map = (Map<String, Object>) dataSnapshot.getValue();
                            String value = map.toString();
                            Log.d("TAG", "Value is: " + value);
                            //
                            arrayList = new ArrayList<>();
                            /*for (Map obj: map)
                            {
                                arrayList.add(new Item("Slot 1", R.drawable.ic_launcher_background, "#A14CAF50"));
                            }*/
                    /*    }

                        @Override
                        public void onCancelled(DatabaseError databaseError) {
                            Log.w("failed", "Failed to read value.", databaseError.toException());
                        }
                    });*/
                }
                else {
                    Toast.makeText(getContext(),"Please Select Location",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
    public void openDisplaySlotsActivity()
    {
        Fragment fragment = new DisplaySlots();
        android.support.v4.app.FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();

        fragmentTransaction.replace(R.id.mainLayout,fragment).addToBackStack(null);
        fragmentTransaction.commit();
    }
}
