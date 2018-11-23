package com.example.helly_jainee.publicparking;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.Display;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class DisplaySlots extends Fragment {

    private RecyclerView recyclerView;
    private ArrayList<Item> arrayList;
    FirebaseDatabase database;
    DatabaseReference myRef;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.display_slots,null);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        arrayList = new ArrayList<Item>();
        recyclerView = (RecyclerView) view.findViewById(R.id.rvdisplay);
        Log.d("TAG", "Value is: " + SelectLocation.selectedloc);
        database = FirebaseDatabase.getInstance();
        myRef = database.getReference(SelectLocation.selectedloc);
        //arrayList.add(new Item("slot","#A14CAF50"));
        //arrayList.add(new Item("slot","#A14CAF50"));
        final int flag_notify = 0; //indicates stop notification
        myRef.addValueEventListener(new ValueEventListener() {
                                        @Override
                                        public void onDataChange(DataSnapshot dataSnapshot) {
                                            for( DataSnapshot child : dataSnapshot.getChildren())
                                            {
                                                Log.d("TAG", "Value is: " + child.getKey());
                                                if(child.getValue().toString().equalsIgnoreCase("false"))
                                                {
                                                    int flag = 0;
                                                    for(Item i : arrayList )
                                                    {
                                                        if (i.getText().equalsIgnoreCase(child.getKey()))
                                                        {
                                                            i.setColor("#A14CAF50");
                                                            flag =1;
                                                            break;
                                                        }
                                                    }
                                                    if(flag == 0)
                                                        arrayList.add(new Item(child.getKey(),"#A14CAF50"));
                                                }
                                                else{
                                                    int flag = 0;
                                                    for(Item i : arrayList )
                                                    {
                                                        if (i.getText().equalsIgnoreCase(child.getKey()))
                                                        {
                                                            i.setColor("#A5DE1818");
                                                            flag =1;
                                                            break;
                                                        }
                                                    }
                                                    if(flag == 0)
                                                        arrayList.add(new Item(child.getKey(),"#A5DE1818"));
                                                }
                                            }
                                            HomeAdapter adapter = new HomeAdapter(getContext(), arrayList);
                                            recyclerView.setAdapter(adapter);

                                            GridLayoutManager manager = new GridLayoutManager(getContext(), 2, GridLayoutManager.VERTICAL, false);
                                            recyclerView.setLayoutManager(manager);
                                        }

                                        @Override
                                        public void onCancelled(DatabaseError databaseError) {

                                        }
                                    });
        //arrayList.add(new Item("Slot 1", R.drawable.ic_launcher_background, "#"));

    }
}
