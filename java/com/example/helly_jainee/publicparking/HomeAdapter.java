package com.example.helly_jainee.publicparking;

import android.content.Context;
import android.graphics.Color;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.example.helly_jainee.publicparking.R;
import com.example.helly_jainee.publicparking.Item;

import java.util.ArrayList;

/*
 * Created by Sambhaji Karad on 04-Jan-18
 * Mobile 9423476192
 * Email sambhaji2134@gmail.com/
 */

public class HomeAdapter extends RecyclerView.Adapter<HomeAdapter.ViewHolder> {

    private ArrayList<Item> mValues;
    private Context mContext;
    protected ItemListener mListener;

    public HomeAdapter(Context context, ArrayList<Item> values) {
        mValues = values;
        mContext = context;
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

        private TextView textView;
        private RelativeLayout relativeLayout;
        private Item item;

        public ViewHolder(View v) {
            super(v);
            textView = (TextView) v.findViewById(R.id.tvRow);
            //imageView = (ImageView) v.findViewById(R.id.imageView);
            relativeLayout = (RelativeLayout) v.findViewById(R.id.rlRow);
        }

        public void setData(Item item) {
            this.item = item;
            textView.setText(item.getText());
            //imageView.setImageResource(item.drawable);
            relativeLayout.setBackgroundColor(Color.parseColor(item.color));
        }

    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(mContext).inflate(R.layout.row_item, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(ViewHolder viewHolder, int position) {
        viewHolder.setData(mValues.get(position));
    }

    @Override
    public int getItemCount() {
        return mValues.size();
    }

    public interface ItemListener {
        void onItemClick(Item item);
    }
}
